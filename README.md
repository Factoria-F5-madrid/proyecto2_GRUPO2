## 1. Instalación de Django.
Lo primero será crear una carpeta en nuestro sistema de ficheros para realizar este tutorial. La llamaremos “floristeria”

```
mkdir tutorial
cd tutorial
```


### Antes de la instalación, procedemos a crear un entorno virtual, para lo cual utilizamos el Python Package Installer (pip). Si pip no está instalado en tu equipo, instálalo desde tu terminal con:

```
sudo apt install python3-pip (para Sistemas Operativos basados en Linux debian)
```

```
python -m pip install -U pip (para Windows)
```

### Con pip instalado ya podemos crear el entorno virtual (para luego en él instalar el paquete de python llamado Django)

```
python -m venv venv
```

Ahora debemos activar el entorno virtual recién creado:

```
source venv/bin/activate (para Sistemas Operativos basados en Linux debian)
```

```
.\venv\Scripts\activate.ps1 (Windows)
```

### Ahora ya podemos instalar el paquete de python Django en este entorno virtual:

```
pip install django
```

## 2. Configuración inicial de Django

```
django-admin startproject crudflorist
```

### Vamos a comprobar que nuestro proyecto creado con Django funciona correctamente, para ello ejecutamos

```
cd crudflorist
python manage.py runserver
```

### Debemos crear la app dentro del proyecto

```
python manage.py startapp floristapp
```

### Comando inicial para administración interna de Django

```
python manage.py migrate
````



