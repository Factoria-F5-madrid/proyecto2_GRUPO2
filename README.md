## 1. Instalación de Django.
Lo primero será crear una carpeta en nuestro sistema de ficheros para realizar este tutorial. La llamaremos “floristeria”

```
mkdir florist
cd florist
```


### Antes de la instalación, procedemos a crear un entorno virtual, para lo cual utilizamos el Python Package Installer (pip). Si pip no está instalado en tu equipo, instálalo desde tu terminal con:

```
sudo apt install python3-pip (para Sistemas Operativos basados en Linux debian)
```

```
python -m pip install -U pip (para Windows siempre ejecutaremos "python" en vez de "python3")
```

### Con pip instalado ya podemos crear el entorno virtual (para luego en él instalar el paquete de python llamado Django)

```
python3 -m venv .venv
```

Ahora debemos activar el entorno virtual recién creado:

```
source .venv/bin/activate (para Sistemas Operativos basados en Linux debian)
```

```
.\.venv\Scripts\activate.ps1 (Windows)
```

### Ahora ya podemos instalar el paquete de python Django en este entorno virtual:

```
pip install django
```

- Tenemos que tener la versión Django 5.2.4

## 2. Configuración inicial de Django

```
django-admin startproject crudflorist
```

### Vamos a comprobar que nuestro proyecto creado con Django funciona correctamente, para ello ejecutamos

```
cd crudflorist
```
### Ejecutar el servidor de Django en segundo plano


```bash
python3 manage.py runserver &
```

Ver los procesos en segundo plano:

```
jobs
```

Esto mostrará una lista como:

```
[1]+  Running		 python3 manage.py runserver &

```

Pasar un proceso al primer plano (foreground):

```
fg <número del job>
```

Por ejemplo:

```
fg %1
```

Pasar un proceso de foreground a background:

Si tienes un proceso corriendo en primer plano y quieres enviarlo al segundo plano:

Primero pausa el proceso con Ctrl + Z
Esto lo suspende temporalmente.
Luego reanúdalo en background con:

```
bg
```


### Debemos crear la app dentro del proyecto

```
python3 manage.py startapp floristapp
```

### Comando inicial para administración interna de Django

```
python3 manage.py migrate
```
