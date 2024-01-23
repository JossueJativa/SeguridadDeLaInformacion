@echo off
setlocal enabledelayedexpansion

REM Verificar la política de ejecución actual
set POLICY=
for /f "tokens=* USEBACKQ" %%F in (`powershell Get-ExecutionPolicy`) do set POLICY=%%F

echo La política de ejecución actual es: %POLICY%

REM Verificar si la política actual es "Restricted"
if /i "%POLICY%"=="Restricted" (
    echo La política actual es Restringida.
    
    REM Intentar establecer la política a "Bypass"
    echo Intentando establecer la política a "Bypass"...
    powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force"

    REM Verificar nuevamente la política después de intentar ajustarla
    set POLICY=
    for /f "tokens=* USEBACKQ" %%F in (`powershell Get-ExecutionPolicy`) do set POLICY=%%F

    echo Nueva política de ejecución: %POLICY%
)

REM Verificar si la política es "AllSigned" o "Bypass" y realizar la instalación de Chocolatey
if /i "%POLICY%"=="AllSigned" (
    echo La política de ejecución es AllSigned. No se requieren cambios.
) else (
    if /i "%POLICY%"=="Bypass" (
        echo La política de ejecución es Bypass. No se requieren cambios.
    ) else (
        echo La política de ejecución no es AllSigned ni Bypass. Intentando establecerla a "Bypass"...
        powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force"
    )
)

REM Verificar si se está ejecutando como administrador
NET FILE >nul 2>&1
if %errorLevel% == 0 (
    echo El script se está ejecutando como administrador.
) else (
    echo El script no se está ejecutando como administrador. Intentando ejecutar como administrador...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit /B
)

REM Instalar Chocolatey con la respuesta 'Y'
echo Instalando Chocolatey...
echo Y | choco install chocolatey

REM Instalar Docker Desktop con la respuesta 'Y'
echo Instalando Docker Desktop...
echo Y | choco install docker-desktop

REM Construir la imagen Docker
echo Construyendo la imagen Docker...
docker build -t seguridad .

REM Iniciar el contenedor Docker
echo Iniciando el contenedor Docker...
docker run -d -p 8000:8000 seguridad

REM Esperar un momento antes de abrir el navegador web
timeout /t 10

REM Abrir el navegador web en el puerto localhost:8000
echo Abriendo el navegador web en el puerto 8000...
start "" "http://localhost:8000"

echo Espera un momento para que se complete la instalación, construcción y ejecución del contenedor.
pause
