# Login y Registro con Firebase y Flet

Este proyecto implementa un sistema de autenticación completo utilizando Firebase como backend y Flet para la interfaz de usuario. Incluye funcionalidades de registro, inicio de sesión, recuperación de contraseña y gestión de perfil de usuario.

## Características

- Inicio de sesión
- Registro de usuarios
- Recuperación de contraseña
- Perfil de usuario con opción de actualización

## Capturas de pantalla

### Pantalla de Inicio de Sesión

![Imagen de la pantalla de inicio de sesión](https://github.com/ParcivalDev/Flet-Login/blob/main/login-firebase/images/login.png)

### Pantalla de Registro

![Imagen de la pantalla de registro](https://github.com/ParcivalDev/Flet-Login/blob/main/login-firebase/images/register.png)

### Pantalla de Perfil de Usuario

![Imagen de la pantalla de perfil de usuario](https://github.com/ParcivalDev/Flet-Login/blob/main/login-firebase/images/perfil.png)
![Imagen de la pantalla de perfil de usuario](https://github.com/ParcivalDev/Flet-Login/blob/main/login-firebase/images/perfil2.png)

### Página Web de Recuperación de Contraseña

![Imagen de la página web de recuperación de contraseña](https://github.com/ParcivalDev/Flet-Login/blob/main/login-firebase/images/recu_pass.png)

## Configuración Inicial

1. Clonar el repositorio.
2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar dependencias:

   ```bash
   pip install flet
   pip install firebase-admin
   ```

## Configuración de Firebase

### Crear Proyecto en Firebase

1. Ve a la [Web de Firebase](https://firebase.google.com/).
2. Haz clic en "Añadir proyecto" y sigue los pasos.

### Authentication

1. En el menú lateral de la consola de Firebase, ve a "Authentication".
2. En la pestaña "Método de acceso", habilita el proveedor de "Correo electrónico/contraseña".

### Realtime Database

1. En el menú lateral, selecciona "Realtime Database".
2. Haz clic en "Crear base de datos" y elige la ubicación.
3. Inicia en modo de prueba.
4. En la pestaña "Reglas", configura las siguientes reglas de seguridad:

   ```json
   {
     "rules": {
       "users": {
         "$uid": {
           ".read": "$uid === auth.uid",
           ".write": "$uid === auth.uid"
         }
       }
     }
   }
   ```

### Obtener Credenciales

1. En la configuración del proyecto (ícono de engranaje), ve a "Cuentas de servicio".
2. Haz clic en "Generar nueva clave privada". Esto descargará un archivo JSON.
3. Guarda este archivo en un lugar seguro dentro de tu proyecto (por ejemplo, en una carpeta `config`).

### Crear Aplicación Web y Obtener API Key

1. En la configuración del proyecto, haz clic en "Agregar app" tipo web.
2. Después de registrar la app, se te mostrará un objeto de configuración. Busca la línea que comienza con `apiKey:`. Copia el valor de `apiKey`. Este es tu FIREBASE_API_KEY.

## Configuración de Variables de Entorno

Crea un archivo `.env` en la raíz de tu proyecto con el siguiente contenido:

```env
FIREBASE_CONFIG_PATH=/ruta/completa/al/archivo/firebase_config.json
FIREBASE_API_KEY=tu_api_key
FIREBASE_DATABASE_URL=https://tu-proyecto.firebaseio.com
```

Donde:

- `FIREBASE_CONFIG_PATH`: Es la ruta completa al archivo JSON de configuración que descargaste.
- `FIREBASE_API_KEY`: Es el valor de `apiKey` que copiaste al crear la aplicación web.
- `FIREBASE_DATABASE_URL`: Es la URL de tu Realtime Database, visible en la sección de Realtime Database en la consola de Firebase.

> **IMPORTANTE**
    > - Nunca subas el archivo `.env` o el archivo JSON de configuración de Firebase a un repositorio.
    > - Asegúrate de que el archivo `.env` esté incluido en tu `.gitignore`.
