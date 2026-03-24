## Creamos en entorno virtual

```sh
python -m venv venv
```
 
## Activa entorno virtual 

```sh
.\venv\Scripts\activate
```
## instala django (importante tener activado entorno)
```sh
 pip install django
```

## Creas el proyecto

```sh
django-admin startproject clinica_veterinaria .
```

## Con esto creas la app

```sh
 python manage.py startapp pacientes
```

## Necesitamos instalar el driver conexion (importante tener activado entorno)

```sh
pip install django psycopg2-binary
```

## Ver cuales son las dependencias de tu proyecto de Django

```sh
pip freeze
```

## Si quieres guardar esas depedencias en un archivo como requirements.txt

```sh
pip freeze > requirements.txt
```

## Como instalo las depedencias descritas en requirements.txt? (importante tener activado entorno)

```sh
pip install -r requirements.txt
```


## Instalaciones para encriptacion de passwords (importante tener activado entorno)
 
```sh
pip install bcrypt
```


```sh
pip install argon2-cffi
```