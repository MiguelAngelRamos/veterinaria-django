1. Crear las migraciones

```sh
python manage.py makemigrations
```
¿Que hace? Este comando examina nuestro models.py, busca cualquier cualquier cambio que hayas hecho (agregar nuevo campo, quitar un campo, modificar un tipo de datos) y esto va generar un nuevo archivo en la carpeta **migrations** y este archivo va contener las intrucciones en codigo python de como transformar la base datos en ese nuevo estado. (Es equivalente a escribir un guion de lo que va pasar en la base de datos)


2. migrate

```sh
python manage.py migrate
```
¿Que hace? toma el **"guion"** generado en el paso 1 y los va ejecutar traduciendolos en codigo SQL real en el gestor de base de datos que estes utilizando. (POSTGRESQL, MYSQL, SQLSERVER, ORACLE), **es este comando el que hace el cambio fisico** en nuestra estructura de base de datos