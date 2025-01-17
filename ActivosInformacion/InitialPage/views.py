import base64
import io
import json
import pyotp
import qrcode

from google.cloud import kms
from google.oauth2 import service_account

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from InitialPage.models import Departments, Assets, AssetsDependence, AssetsValue, TypeAssets, SubtypeAssets, Risk, AssetsRisk, RiskType, Safeguards, SafeguardsRisk, SafeguardsTypes
from Users.models import User, Workload

from google.oauth2 import service_account
from google.cloud import kms

credential_path = "C://Users//user//GitRepositories//UDLA//SeguridadDeLaInformacion//ActivosInformacion//InitialPage//mysiteseg-d844acd475b8.json"
credentials = service_account.Credentials.from_service_account_file(credential_path)
kms_client = kms.KeyManagementServiceClient(credentials=credentials)

# Configuración del proyecto y la clave
project_id = "mysiteseg"
location_id = "global"
key_ring_id = "activos-informacion"
crypto_key_id = "activos-informacion"

# Create your views here.
def generate_asset_code():
    # Obtén el último código almacenado en la base de datos
    last_asset = Assets.objects.last()

    if last_asset:
        last_code = last_asset.code
        prefix = last_code[:-4]  # Obtiene los primeros dos caracteres (por ejemplo, 'AA')
        number = int(last_code[-4:]) + 1  # Obtiene los últimos cuatro caracteres y les suma 1
        if number > 9999:
            # Si el número excede 9999, cambia a la siguiente combinación de letras
            prefix = chr(ord(prefix[0]) + 1) + prefix[1]  # Cambia la primera letra a la siguiente en el alfabeto
            number = 1  # Reinicia el número a 1

        new_code = f"{prefix}{number:04d}"  # Formatea el nuevo código
    else:
        # Si no hay ningún registro en la base de datos, comienza desde el principio
        new_code = "AA0001"

    return new_code

def userProfile(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        otp = request.POST.get("otp")

        try:
            user = User.objects.get(pk=user_id)
            totp = pyotp.TOTP(user.mfa_secret)
            if totp.verify(otp):
                user.mfa_enabled = True
                user.save()
                return render(request, "user/perfil.html", {
                    "user": user,
                    "message": "Autenticación de dos factores activada"
                })
        except User.DoesNotExist:
            return render(request, "user/perfil.html", {
                "message": "Usuario no encontrado"
            })
        except pyotp.TOTPError:
            return render(request, "user/perfil.html", {
                "message": "Código de autenticación inválido"
            })

    else:
        user = User.objects.get(pk=request.user.id)
        if not user.mfa_secret:
            user.mfa_secret = pyotp.random_base32()
            user.save()

        otp_uri = pyotp.totp.TOTP(user.mfa_secret).provisioning_uri(
            name=user.username,
            issuer_name="Activos Información"
        )

        qr = qrcode.make(otp_uri)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")

        buffer.seek(0)
        qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")
        qr_code_data_uri = f"data:image/png;base64,{qr_code}"

        return render(request, "user/perfil.html", {
            "user": user,
            "qr_code": qr_code_data_uri
        })

def enterAsset(request):
    if request.user.is_authenticated:
        departmentsName = Departments.objects.values('name').distinct()

        # Crear id para cada departamento
        for department in departmentsName:
            department['id'] = Departments.objects.filter(name=department['name']).first().id

        if request.method == "POST":
            # Informacion inicial
            code = request.POST.get("code")
            name = request.POST.get("name")
            type = request.POST.get("type")
            subtype = request.POST.get("subtype")
            responsableArea = request.POST.get("responsableArea")
            responsablePerson = request.POST.get("responsablePerson")
            ubicationType = request.POST.get("ubicationType")
            ubication = request.POST.get("ubication")
            quantity = request.POST.get("quantity")
            characteristic = request.POST.get("characteristic")

            # Verificacion de toggles
            state = request.POST.get("state")
            state2 = request.POST.get("state2")

            #Guardar el activo
            try:
                asset = Assets(
                    code = code,
                    name = name,
                    ubicationType = ubicationType,
                    ubication = ubication,
                    quantity = quantity,
                    characteristic = characteristic,
                    type = TypeAssets.objects.get(pk=type),
                    responsableArea = Departments.objects.get(pk=responsableArea),
                    responsableUser = User.objects.get(pk=responsablePerson)
                )
                asset.save()
            except Exception as e:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": f"Error al ingresar el activo {e}"
                })
            
            if state == "on":
                #Informacion de dependencias
                dependency = request.POST.get("dependency")
                descriptionDependency = request.POST.get("descriptionDependency")
                responsableUser = request.POST.get("responsableUser")
                dependsOf = request.POST.get("dependsOf")

                if dependency == "" or dependency == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle
                        "state": state,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        "message": "Seleccione la dependencia",
                    })
                
                if descriptionDependency == "" or descriptionDependency == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle
                        "state": state,
                        "dependency": dependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        "message": "Ingrese la descripción de la dependencia",
                    })
                
                if responsableUser == "" or responsableUser == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "dependsOf": dependsOf,
                        "message": "Seleccione el responsable del activo"
                    })
                
                if dependsOf == "" or dependsOf == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle 1
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "message": "Seleccione de que depende"
                    })
                
                responsableUser = User.objects.get(pk=responsableUser)
                dependsOf = Assets.objects.get(pk=dependsOf)

                try:
                    assetDependence = AssetsDependence(
                        percentaje = dependency,
                        asset = asset,
                        responsableUser = responsableUser,
                        assetDepend = dependsOf
                    )
                    assetDependence.save()
                except Exception as e:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle 1
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        "message": f"Error al ingresar la dependencia {e}"
                    })

            if state2 == "on":
                # Informacion de valoracion
                valorationDimention = request.POST.get("valorationDimention")
                valorationAssing = request.POST.get("valorationAssing")
                cualitative = request.POST.get("cualitative")
                descriptionValue = request.POST.get("descriptionValue")
                
                if valorationDimention == "" or valorationDimention == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        "message": "Seleccione la dimensión de valoración"
                    })
                
                if valorationAssing == "" or valorationAssing == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        "message": "Seleccione la valoración"
                    })
                
                try:
                    assetValue = AssetsValue(
                        cuantityValue = valorationAssing,
                        cualityValue = cualitative,
                        description = descriptionValue,
                        dimentionValue = valorationDimention,
                        asset = asset
                    )
                    assetValue.save()
                except Exception as e:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        "message": f"Error al ingresar la valoración {e}"
                    })
                
                try:
                    # ver si los otros campos estan llenos para guardarlos o no
                    # Primeros campos
                    valorationDimention2 = request.POST.get("valorationDimention2")
                    valorationAssing2 = request.POST.get("valorationAssing2")
                    subtype= SubtypeAssets.objects.get(pk=subtype)
                    if valorationDimention2 != None or valorationDimention2 != "" or valorationAssing2 != None or valorationAssing2 != "":
                        descriptionValue2 = request.POST.get("descriptionValue2")
                        cualitative2 = request.POST.get("cualitative2")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing2,
                                cualityValue = cualitative2,
                                description = descriptionValue2,
                                dimentionValue = valorationDimention2,
                                asset = asset,
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                            })
                except Exception as e:
                    pass
                    
                try:
                    # ver si los otros campos estan llenos para guardarlos o no
                    # Segundos campos
                    valorationDimention3 = request.POST.get("valorationDimention3")
                    valorationAssing3 = request.POST.get("valorationAssing3")

                    if valorationDimention3 != None or valorationDimention3 != "" or valorationAssing3 != None or valorationAssing3 != "":
                        descriptionValue3 = request.POST.get("descriptionValue3")
                        cualitative3 = request.POST.get("cualitative3")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing3,
                                cualityValue = cualitative3,
                                description = descriptionValue3,
                                dimentionValue = valorationDimention3,
                                asset = asset
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                                "responsableUser": responsableUser
                            })
                except Exception as e:
                    pass

                try:
                    valorationDimention4 = request.POST.get("valorationDimention4")
                    valorationAssing4 = request.POST.get("valorationAssing4")

                    if valorationDimention4 != None or valorationDimention4 != "" or valorationAssing4 != None or valorationAssing4 != "":
                        descriptionValue4 = request.POST.get("descriptionValue4")
                        cualitative4 = request.POST.get("cualitative4")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing4,
                                cualityValue = cualitative4,
                                description = descriptionValue4,
                                dimentionValue = valorationDimention4,
                                asset = asset
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                                "responsableUser": responsableUser
                            })
                except Exception as e:
                    pass

                try:
                    valorationDimention5 = request.POST.get("valorationDimention5")
                    valorationAssing5 = request.POST.get("valorationAssing5")

                    if valorationDimention5 != None or valorationDimention5 != "" or valorationAssing5 != None or valorationAssing5 != "":
                        descriptionValue5 = request.POST.get("descriptionValue4")
                        cualitative5 = request.POST.get("cualitative4")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing5,
                                cualityValue = cualitative5,
                                description = descriptionValue5,
                                dimentionValue = valorationDimention5,
                                asset = asset
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                                "responsableUser": responsableUser,
                            })
                except Exception as e:
                    pass

            return render(request, "tables/assets.html",{
                "DependentAssets": AssetsDependence.objects.all(),
                "AssetsValue": AssetsValue.objects.all()
            })
        else:
            codigo_auto = generate_asset_code()
            return render(request, "home/enterAsset.html",{
                "code": codigo_auto,
                "Departments": departmentsName,
                "Users": User.objects.all(),
                "Assets": Assets.objects.all(),
                "TypeAssets": TypeAssets.objects.all(),
                "SubtypeAssets": SubtypeAssets.objects.all()
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def tableAssets(request):
    if request.user.is_authenticated:
        return render(request, "tables/assets.html",{
            "DependentAssets": AssetsDependence.objects.all(),
            "AssetsValues": AssetsValue.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def editTableAssets(request):
    if request.method == "POST":
        # Obtener todos los departamentos sin nombres duplicados
        departmentsName = Departments.objects.values('name').distinct()

        # Crear id para cada departamento
        for department in departmentsName:
            department['id'] = Departments.objects.filter(name=department['name']).first().id

        if request.method == "POST":
            # Informacion inicial
            assetValueID = request.POST.get("assetValueID")
            assetId = request.POST.get("assetId")
            code = request.POST.get("code")
            name = request.POST.get("name")
            type = request.POST.get("type")
            subtype = request.POST.get("subtype")
            responsableArea = request.POST.get("responsableArea")
            responsablePerson = request.POST.get("responsablePerson")
            ubicationType = request.POST.get("ubicationType")
            ubication = request.POST.get("ubication")
            quantity = request.POST.get("quantity")
            characteristic = request.POST.get("characteristic")

            # Verificacion de toggles
            state2 = request.POST.get("state2")

            asset = Assets.objects.get(pk=assetId)

        if state2 == "on":
            # Informacion de valoracion
            valorationDimention = request.POST.get("valorationDimention")
            valorationAssing = request.POST.get("valorationAssing")
            cualitative = request.POST.get("cualitative")
            descriptionValue = request.POST.get("descriptionValue")
            
            if valorationDimention == "" or valorationDimention == None:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": "Seleccione la dimensión de valoración"
                })
            
            if valorationAssing == "" or valorationAssing == None:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": "Seleccione la valoración"
                })
            
            try:
                # Actualizar asset value
                AssetsValue.objects.filter(pk=assetValueID).update(
                    cuantityValue = valorationAssing,
                    cualityValue = cualitative,
                    description = descriptionValue,
                    dimentionValue = valorationDimention,
                    asset = asset
                )
            except Exception as e:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": f"Error al ingresar la valoración {e}"
                })
        # Actializar campos
        try:
            Assets.objects.filter(pk=asset.id).update(
                code = code,
                name = name,
                ubicationType = ubicationType,
                ubication = ubication,
                quantity = quantity,
                characteristic = characteristic,
                type = TypeAssets.objects.get(pk=type),
                responsableArea = Departments.objects.get(pk=responsableArea),
                responsableUser = User.objects.get(pk=responsablePerson)
            )
        except Exception as e:
            return render(request, "home/enterAsset.html",{
                "Departments": departmentsName,
                # Parte principal
                "code": code,
                "name": name,
                "type": type,
                "subtype": subtype,
                "responsableArea": responsableArea,
                "responsablePerson": responsablePerson,
                "ubicationType": ubicationType,
                "ubication": ubication,
                "quantity": quantity,
                "characteristic": characteristic,
                "message": f"Error al ingresar el activo {e}"
            })

        return render(request, "tables/assets.html",{
            "DependentAssets": AssetsDependence.objects.all(),
            "AssetsValue": AssetsValue.objects.all()
        })   

def deleteTableAssets(request, id):
    if request.user.is_authenticated:
        try:
            asset = Assets.objects.get(pk=id)
            # Eliminar las dependencias
            assetsDependence = AssetsDependence.objects.filter(assetDepend=asset)
            for assetDependence in assetsDependence:
                assetDependence.delete()

            # Eliminar los valores
            assetsValue = AssetsValue.objects.filter(asset=asset)
            for assetValue in assetsValue:
                assetValue.delete()
            asset.delete()
        except Exception as e:
            return render(request, "tables/assets.html",{
                "DependentAssets": AssetsDependence.objects.all(),
                "AssetsValue": AssetsValue.objects.all(),
                "message": f"Error al eliminar el activo {e}"
            })
        
        return render(request, "tables/assets.html",{
            "DependentAssets": AssetsDependence.objects.all(),
            "AssetsValue": AssetsValue.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def enterUsers(request):
    if request.user.is_authenticated:
        # Obtener todos los departamentos sin nombres duplicados
        departmentsName = Departments.objects.values('name').distinct()

        # Crear id para cada departamento
        for department in departmentsName:
            department['id'] = Departments.objects.filter(name=department['name']).first().id

        if request.method == "POST":
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            celular = request.POST.get("phone")
            password = request.POST.get("password")
            confirm = request.POST.get("confirm")
            userDepartment = request.POST.get("userDepartment")
            workload = request.POST.get("workload")

            if firstname == "" or firstname == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese el nombre del usuario"
                })
            
            if lastname == "" or lastname == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese el apellido del usuario"
                })
            
            if email == "" or email == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese el correo del usuario"
                })
            
            if celular == "" or celular == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese la identidad del usuario"
                })
            
            if password == "" or password == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese la contraseña del usuario"
                })
            
            if confirm == "" or confirm == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Confirme la contraseña del usuario"
                })
            
            if userDepartment == "" or userDepartment == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Seleccione el departamento del usuario"
                })
            
            if workload == "" or workload == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Seleccione la carga de trabajo del usuario"
                })
            
            if password != confirm:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Las contraseñas no coinciden"
                })
            
            workload = Workload.objects.get(pk=workload)
            userDepartment = Departments.objects.get(pk=userDepartment)

            try:
                department = Departments(
                    name = userDepartment.name,
                    description = userDepartment.description,
                    workload = workload
                )
                department.save()
            except Exception as e:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": f"Error al ingresar el departamento {e}"
                })
            
            try:
                idlastUser = User.objects.last()
            except:
                idlastUser = 1
            
            username = f"{firstname}.{lastname}.{idlastUser.id}"

            try:
                user = User.objects.create_user(
                    first_name = firstname,
                    last_name = lastname,
                    email = email,
                    celular = celular,
                    password = password,
                    workload = workload,
                    username= username,
                    department = department.name
                )
                user.save()
            except Exception as e:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": f"Error al ingresar el usuario {e}"
                })
            
            return render(request, "tables/users.html",{
                "Users": User.objects.all(),
            })
        return render(request, "home/enterUsers.html",{
            "Workloads": Workload.objects.all(),
            "Departments": departmentsName
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tableusers(request):
    if request.user.is_authenticated:
        return render(request, "tables/users.html",{
            "Users": User.objects.all(),
            "Departments": Departments.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableUsers(request, id):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(pk=id)
            user.delete()
        except Exception as e:
            return render(request, "tables/users.html",{
                "Users": User.objects.all(),
                "message": f"Error al eliminar el usuario {e}"
            })
        
        return render(request, "tables/users.html",{
            "Users": User.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def editTableUsers(request):
    if request.method == "POST":
        userId = request.POST.get("userId")
        firstname = request.POST.get("userFirstName")
        lastname = request.POST.get("userLastName")
        username = request.POST.get("userUsername")
        email = request.POST.get("userEmail")
        celular = request.POST.get("userCelular")
        userDepartment = request.POST.get("userDepartment")
        workload = request.POST.get("userWorkload")

        if firstname == "" or firstname == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el nombre del usuario"
            })
        
        if lastname == "" or lastname == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el apellido del usuario"
            })
        
        if email == "" or email == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el correo del usuario"
            })
        
        if celular == "" or celular == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el celular del usuario"
            })
        
        if userDepartment == "" or userDepartment == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Seleccione el departamento del usuario"
            })
        
        if workload == "" or workload == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Seleccione la carga de trabajo del usuario"
            })
        
        workload = Workload.objects.get(pk=workload)
        userDepartment = Departments.objects.get(pk=userDepartment)
        try:
            department = Departments(
                name = userDepartment.name,
                description = userDepartment.description,
                workload = workload
            )
            department.save()
        except Exception as e:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": f"Error al ingresar el departamento {e}"
            })
        
        try:
            User.objects.filter(pk=userId).update(
                first_name = firstname,
                last_name = lastname,
                username=username,
                email = email,
                celular = celular,
                workload = workload,
                department = department.name
            )
        except Exception as e:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": f"Error al ingresar el usuario {e}"
            })
        
        return render(request, "tables/users.html",{
            "Users": User.objects.all(),
        })
    else:
        return render(request, "tables/users.html",{
            "Workloads": Workload.objects.all(),
            "Departments": Departments.objects.all()
        })

def enterDepartment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            departmentName = request.POST.get("departmentName")
            description = request.POST.get("description")
            workload = request.POST.get("workload")

            if departmentName == "" or departmentName == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese el nombre del departamento"
                })
            
            if description == "" or description == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese la descripción del departamento"
                })
            
            if workload == "" or workload == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese la carga de trabajo del departamento"
                })

            workload = Workload.objects.get(pk=workload)

            try:
                department = Departments(
                    name = departmentName,
                    description = description,
                    workload = workload
                )
                department.save()
            except Exception as e:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": f"Error al ingresar el departamento {e}"
                })
            
            return render(request, "tables/departaments.html",{
                "Departments": Departments.objects.all(),
            })
        else:
            return render(request, "home/enterDepartment.html",{
                "Workloads": Workload.objects.all()
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tabledepartments(request):
    if request.user.is_authenticated:
        return render(request, "tables/departaments.html",{
            "Departments": Departments.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableDepartments(request, id):
    if request.user.is_authenticated:
        try:
            department = Departments.objects.get(pk=id)
            department.delete()
        except Exception as e:
            return render(request, "tables/departaments.html",{
                "Departments": Departments.objects.all(),
                "message": f"Error al eliminar el departamento {e}"
            })
        
        return render(request, "tables/departaments.html",{
            "Departments": Departments.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def editTableDepartments(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            departmentId = request.POST.get("departmentId")
            departmentName = request.POST.get("departmentName")
            description = request.POST.get("description")
            workload = request.POST.get("workload")

            if departmentName == "" or departmentName == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese el nombre del departamento"
                })
            
            if description == "" or description == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese la descripción del departamento"
                })
            
            if workload == "" or workload == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese la carga de trabajo del departamento"
                })

            workload = Workload.objects.get(pk=workload)

            try:
                Departments.objects.filter(pk=departmentId).update(
                    name = departmentName,
                    description = description,
                    workload = workload
                )
            except Exception as e:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": f"Error al ingresar el departamento {e}"
                })
            
            return render(request, "tables/departaments.html",{
                "Departments": Departments.objects.all(),
            })
        else:
            return render(request, "home/enterDepartment.html",{
                "Workloads": Workload.objects.all()
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def asingRiskAsset(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            asset = request.POST.get("asset")
            risk = request.POST.get("risk")
            impact = request.POST.get("impact")
            probability = request.POST.get("probability")
            selected_risks = request.POST.getlist("selectedRisks")
            risks = []

            if asset == "" or asset == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if risk == "" or risk == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el riesgo"
                })
            
            if selected_risks == "" or selected_risks == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione los riesgos"
                })
            
            if impact == "" or impact == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el impacto"
                })
            
            if probability == "" or probability == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione la probabilidad"
                })
            
            asset = Assets.objects.get(pk=asset)
            risk = RiskType.objects.get(pk=risk)

            for selected_risk in selected_risks:
                risks.append(Risk.objects.get(pk=selected_risk))

            if (impact == "MA" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "M"):
                dimention = "M"
            elif (impact == "B" and probability == "B"):
                dimention = "B"
            elif (impact == "MB" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MA" and probability == "A"):
                dimention = "MA"
            elif (impact == "MA" and probability == "M"):
                dimention = "MA"
            elif (impact == "MA" and probability == "B"):
                dimention = "MA"
            elif (impact == "MA" and probability == "MB"):
                dimention = "A"
            elif (impact == "A" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "M"):
                dimention = "A"
            elif (impact == "A" and probability == "B"):
                dimention = "A"
            elif (impact == "A" and probability == "MB"):
                dimention = "M"
            elif (impact == "M" and probability == "MA"):
                dimention = "A"
            elif (impact == "M" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "B"):
                dimention = "M"
            elif (impact == "M" and probability == "MB"):  
                dimention = "B"
            elif (impact == "B" and probability == "MA"):
                dimention = "M"
            elif (impact == "B" and probability == "A"):
                dimention = "M"
            elif (impact == "B" and probability == "M"):
                dimention = "B"
            elif (impact == "B" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MB" and probability == "MA"):
                dimention = "B"
            elif (impact == "MB" and probability == "A"):
                dimention = "B"
            elif (impact == "MB" and probability == "M"):
                dimention = "MB"
            elif (impact == "MB" and probability == "B"):
                dimention = "MB"
            else:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el impacto y la probabilidad"
                })

            try:
                riskAsset = AssetsRisk(
                    asset=asset,
                    risktype=risk,
                    dimention=dimention
                )
                riskAsset.save()
                riskAsset.risk.set(risks)
            except Exception as e:
                return render(request, "home/enterRisk.html", {
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": f"Error al ingresar el riesgo {e}"
                })

            return render(request, "home/enterRisk.html", {
                "risktypes": RiskType.objects.all(),
                "assets": Assets.objects.all(),
            })
        else:
            return render(request, "home/enterRisk.html", {
                "risktypes": RiskType.objects.all(),
                "assets": Assets.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tableRisks(request):
    if request.user.is_authenticated:
        return render(request, "tables/risk.html",{
            "AssetsRisk": AssetsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableRisks(request, id):
    if request.user.is_authenticated:
        try:
            risk = AssetsRisk.objects.get(pk=id)
            risk.delete()
        except Exception as e:
            return render(request, "tables/risk.html",{
                "AssetsRisk": AssetsRisk.objects.all(),
                "message": f"Error al eliminar el riesgo {e}"
            })
        
        return render(request, "tables/risk.html",{
            "AssetsRisk": AssetsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def editTableRisks(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            riskId = request.POST.get("riskId")
            asset = request.POST.get("asset")
            risk = request.POST.get("risk")
            impact = request.POST.get("impact")
            probability = request.POST.get("probability")
            selected_risks = request.POST.getlist("selectedRisks")
            risks = []

            if asset == "" or asset == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if risk == "" or risk == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el riesgo"
                })
            
            if selected_risks == "" or selected_risks == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione los riesgos"
                })
            
            asset = Assets.objects.get(pk=asset)
            risk = RiskType.objects.get(pk=risk)

            for selected_risk in selected_risks:
                risks.append(Risk.objects.get(pk=selected_risk))

            if (impact == "MA" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "M"):
                dimention = "M"
            elif (impact == "B" and probability == "B"):
                dimention = "B"
            elif (impact == "MB" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MA" and probability == "A"):
                dimention = "MA"
            elif (impact == "MA" and probability == "M"):
                dimention = "MA"
            elif (impact == "MA" and probability == "B"):
                dimention = "MA"
            elif (impact == "MA" and probability == "MB"):
                dimention = "A"
            elif (impact == "A" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "M"):
                dimention = "A"
            elif (impact == "A" and probability == "B"):
                dimention = "A"
            elif (impact == "A" and probability == "MB"):
                dimention = "M"
            elif (impact == "M" and probability == "MA"):
                dimention = "A"
            elif (impact == "M" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "B"):
                dimention = "M"
            elif (impact == "M" and probability == "MB"):  
                dimention = "B"
            elif (impact == "B" and probability == "MA"):
                dimention = "M"
            elif (impact == "B" and probability == "A"):
                dimention = "M"
            elif (impact == "B" and probability == "M"):
                dimention = "B"
            elif (impact == "B" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MB" and probability == "MA"):
                dimention = "B"
            elif (impact == "MB" and probability == "A"):
                dimention = "B"
            elif (impact == "MB" and probability == "M"):
                dimention = "MB"
            elif (impact == "MB" and probability == "B"):
                dimention = "MB"
            else:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el impacto y la probabilidad"
                })

            try:
                AssetsRisk.objects.filter(pk=riskId).update(
                    asset=asset,
                    risktype=risk,
                    dimention=dimention
                )
                riskAsset = AssetsRisk.objects.get(pk=riskId)
                riskAsset.risk.set(risks)
            except Exception as e:
                return render(request, "home/enterRisk.html", {
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": f"Error al ingresar el riesgo {e}"
                })

            return render(request, "tables/risk.html", {
                "AssetsRisk": AssetsRisk.objects.all(),
            })
        else:
            return render(request, "home/enterRisk.html", {
                "risktypes": RiskType.objects.all(),
                "assets": Assets.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def enterSafeguards(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            assetrisk = request.POST.get("assetrisk")
            safeguard = request.POST.get("safeguard")
            addsafeguards = request.POST.getlist("selectedSafeguards")
            safeguards = []
            print(addsafeguards)

            if assetrisk == "" or assetrisk == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if safeguard == "" or safeguard == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione la salvaguarda"
                })
            
            if addsafeguards == "" or addsafeguards == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione las salvaguardas"
                })
            
            assetrisk = AssetsRisk.objects.get(pk=assetrisk)
            safeguard = Safeguards.objects.get(pk=safeguard)

            for addsafeguard in addsafeguards:
                safeguards.append(Safeguards.objects.get(pk=addsafeguard))

            print(safeguards)

            try:
                safeguardAssetRisk = SafeguardsRisk(
                    risk=assetrisk,
                )
                safeguardAssetRisk.save()
                safeguardAssetRisk.safeguard.set(safeguards)
            except Exception as e:
                return render(request, "home/enterSafeguards.html", {
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": f"Error al ingresar la salvaguarda {e}"
                })
            
            return render(request, "home/enterSafeguards.html", {
                "assetsRisk": AssetsRisk.objects.all(),
                "Safeguards": Safeguards.objects.all(),
            })
        else:
            return render(request, "home/enterSafeguards.html",{
                "assetsRisk": AssetsRisk.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tableSafeguards(request):
    if request.user.is_authenticated:
        return render(request, "tables/safeguards.html",{
            "Safeguards": SafeguardsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableSafeguards(request, id):
    if request.user.is_authenticated:
        try:
            safeguard = SafeguardsRisk.objects.get(pk=id)
            safeguard.delete()
        except Exception as e:
            return render(request, "tables/safeguards.html",{
                "Safeguards": SafeguardsRisk.objects.all(),
                "message": f"Error al eliminar la salvaguarda {e}"
            })
        
        return render(request, "tables/safeguards.html",{
            "Safeguards": SafeguardsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def editTableSafeguards(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            safeguardId = request.POST.get("safeguardId")
            asset = request.POST.get("asset")
            selectedSafeguards = request.POST.getlist("selectedSafeguards")
            safeguards = []

            if asset == "" or asset == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if selectedSafeguards == "" or selectedSafeguards == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione las salvaguardas"
                })

            for selectedSafeguard in selectedSafeguards:
                safeguards.append(Safeguards.objects.get(pk=selectedSafeguard))

            try:
                safeguardAssetRisk = SafeguardsRisk.objects.get(pk=safeguardId)
                safeguardAssetRisk.safeguard.set(safeguards)
            except Exception as e:
                return render(request, "home/enterSafeguards.html", {
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": f"Error al ingresar la salvaguarda {e}"
                })
            
            return render(request, "tables/safeguards.html", {
                "Safeguards": SafeguardsRisk.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def get_subtypes(request, type_id):
    subtypes = SubtypeAssets.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(subtypes), safe=False)

def get_workloads(request):
    workloads = Workload.objects.all().values('id', 'name')
    return JsonResponse(list(workloads), safe=False)

def get_departments(request):
    departmentsName = Departments.objects.values('name').distinct()

    # Crear id para cada departamento
    for department in departmentsName:
        department['id'] = Departments.objects.filter(name=department['name']).first().id
    return JsonResponse(list(departmentsName), safe=False)

def get_dependentAssets(request):
    dependentAssets = AssetsDependence.objects.all().values('id', 'asset', 'percentaje', 'assetDepend')
    return JsonResponse(list(dependentAssets), safe=False)

def get_assets(request):
    assets = Assets.objects.all().values('id', 'name')
    return JsonResponse(list(assets), safe=False)

def get_types(request):
    types = TypeAssets.objects.all().values('id', 'name')
    return JsonResponse(list(types), safe=False)

def get_subtypes2(request):
    subtypes = SubtypeAssets.objects.all().values('id', 'name')
    return JsonResponse(list(subtypes), safe=False)

def get_users(request):
    users = User.objects.all().values('id', 'username', 'first_name', 'last_name')
    return JsonResponse(list(users), safe=False)

def get_risks(request, risktype_id):
    risk = Risk.objects.filter(type=risktype_id).values('id', 'name')
    return JsonResponse(list(risk), safe=False)

def get_risktypes(request):
    risktypes = RiskType.objects.all().values('id', 'name')
    return JsonResponse(list(risktypes), safe=False)

def get_safeguardstypes(request):
    safeguardstypes = SafeguardsTypes.objects.all().values('id', 'name')
    return JsonResponse(list(safeguardstypes), safe=False)

def get_safeguards(request, safeguardstype_id):
    safeguards = Safeguards.objects.filter(type=safeguardstype_id).values('id', 'code', 'name')
    return JsonResponse(list(safeguards), safe=False)

def decrypt_with_kms(ciphertext):
    try:
        ciphertext_bytes = base64.b64decode(ciphertext)

        key_name = kms_client.crypto_key_path(
            project_id, location_id, key_ring_id, crypto_key_id
        )

        response = kms_client.decrypt(
            request={"name": key_name, "ciphertext": ciphertext_bytes}
        )

        return response.plaintext.decode("utf-8")
    except Exception as e:
        raise ValueError(f"Error al desencriptar los datos: {e}")

@csrf_exempt
@require_http_methods(["POST"])
def encrypt_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode("utf-8"))
            plaintext_data = data.get('plaintextData')
            if not plaintext_data:
                return JsonResponse({'error': 'El campo data es obligatorio.'}, status=400)
            
            key_name = kms_client.crypto_key_path(
                project_id, location_id, key_ring_id, crypto_key_id
            )

            response = kms_client.encrypt(
                request={"name": key_name, "plaintext": plaintext_data.encode("utf-8")}
            )

            data_encrypted = response.ciphertext
            encrypted_base64 = base64.b64encode(data_encrypted).decode('utf-8')

            return JsonResponse({'encryptedData': encrypted_base64}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Solicitud inválida. Formato JSON incorrecto.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error al encriptar los datos: {e}'}, status=500)
        
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

@csrf_exempt
@require_http_methods(["POST"])
def create_typeAsset(request):
    if request.method == 'POST':
        try:
            # Desencriptar los datos
            encrypted_data = request.body.decode('utf-8')
            decrypted_data = decrypt_with_kms(encrypted_data)
            
            if not decrypted_data:
                return JsonResponse({'error': 'El nombre es obligatorio.'}, status=400)

            new_type_asset = TypeAssets.objects.create(name=decrypted_data)
            return JsonResponse({'message': 'Tipo de activo creado con éxito.', 'id': new_type_asset.id}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Solicitud inválida. Formato JSON incorrecto.'}, status=400)

    return JsonResponse({'error': 'Método no permitido.'}, status=405)