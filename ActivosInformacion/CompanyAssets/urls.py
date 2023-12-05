from django.urls import path
from . import views

app_name = "Assets"

urlpatterns = [
    path("", views.companyassets, name="companyassets"),
    path("editCompanyAssets/", views.editCompanyAssets, name="editCompanyAssets"),
    path("deleteCompanyAssets/<int:id>", views.deleteCompanyAssets, name="deleteCompanyAssets"),
    path("origin/", views.origin, name="origin"),
    path("editOrigin/", views.editOrigin, name="editOrigin"),
    path("deleteOrigin/<int:id>", views.deleteOrigin, name="deleteOrigin"),
    path("companytype/", views.companyType, name="companyType"),
    path("editCompanyType/", views.editcompanyType, name="editCompanyType"),
    path("deleteCompanyType/<int:id>", views.deletecompanyType, name="deleteCompanyType"),
    path('get_subtypes/', views.get_subtypes, name='get_subtypes'),
    path("responsableunity/", views.responsableunity, name="responsableunity"),
    path("editResponsableUnity/", views.editresponsableunity, name="editResponsableUnity"),
    path("deleteResponsableUnity/<int:id>", views.deleteresponsableunity, name="deleteResponsableUnity"),
    path("companyassetsunity/", views.companyunity, name="companyassetsunity"),
    path("editCompanyAssetsUnity/", views.editcompanyunity, name="editCompanyAssetsUnity"),
    path("deleteCompanyAssetsUnity/<int:id>", views.deletecompanyunity, name="deleteCompanyAssetsUnity"),
    path("dependentassets/", views.dependentassets, name="dependentassets"),
    path("editDependentAssets/", views.editdependentassets, name="editDependentAssets"),
    path("deleteDependentAssets/<int:id>", views.deletedependentassets, name="deleteDependentAssets"),
]
