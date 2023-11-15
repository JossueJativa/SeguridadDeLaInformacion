# SeguridadDeLaInformacion

## Comandos para saber
> - django-admin startapp <NombreDeProyecto> //Funciona para crear una nueva app en la aplicacion inicial </br>
> - python manage.py makemigrations //Funciona para ver si las migraciones de las bases de datos funcionan correctamente </br>
> - python manage.py migrate //Funciona para enviar todas las migraciones a la base de datos </br>
> - python manage.py createsuperuser //Funciona para crear un usuario administrador </br>
> - python manage.py collectstatics //Funciona para sacar todos los estilos del proyecto para cuando el proyecto de quite el true del debug </br>
> - python manage.py runserver //Funciona para que el proyecto se ejecute </br>

## Archivos importantes
> - settings.py //Este trae todo lo que el proyecto necesita para funcionar, es decir las aplicaciones, las bases de datos, el lenguaje, etc </br>
> - urls.py //Sirve para poner el path de donde se va a encontrar la pagina web hecha </br>
> - views.py //Sirve para hacer las vistas, donde se toman como clases, el nombre de la clase se debe poner en el urls.py </br>
> - modles.py //Todas las migraciones que se van a hacer a las bases de datos
> - middleware.py //Toda la parte de seguridad del proyecto 
> - test.py //Parte de testeo del proyecto
> - admin.py //Parte de administracion del proyecto y vistas que solo puede hacer el administrador
> - forms.py //Parte de los formularios que se van a hacer en el proyecto
> - apps.py //Parte de las aplicaciones que se van a hacer en el proyecto

## Carpetas importantes del proyecto
> - static //Esta carpeta sirve para guardar todos los estilos, script e imagenes con sus respectivas carpetas </br>
> - templates //Esta carpeta se encarga de guardar todos los html que se hace del sistema </br>

## Funcionalidad del envAct
> - env\Script\activate //Sirve para activar el entorno virtual para windows
> - source env/bin/activate //Sirve para activar el entorno virtual para linux