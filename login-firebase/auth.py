import firebase_admin
from firebase_admin import credentials, auth, db
import os
import requests
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()


# Esta función inicializa la aplicación Firebase
# config_path es la ruta al archivo de configuración de Firebase
def initialize_firebase(config_path):
    cred = credentials.Certificate(config_path)
    # Obtenemos la URL de la base de datos desde las variables de entorno
    database_url = os.getenv('FIREBASE_DATABASE_URL')
    
    if not database_url:
        raise ValueError("FIREBASE_DATABASE_URL no está configurada en las variables de entorno")

    # Inicializamos la aplicación Firebase con las credenciales y la URL de la base de datos
    firebase_admin.initialize_app(cred, {
        'databaseURL': database_url
    })
    return firebase_admin.get_app()  # La aplicación Firebase inicializada


class AuthService:
    def __init__(self, firebase_app):
        self.firebase_app = firebase_app
        # Obtenemos la API key de Firebase de las variables de entorno
        self.api_key = os.getenv("FIREBASE_API_KEY")
        self.user_data = None  # Almacenará los datos del usuario autenticado


    # Registra un nuevo usuario en Firebase
    def register_user(self, email, password):
        try:
            # Intentamos crear un nuevo usuario con el email y password proporcionados
            user = auth.create_user(email=email, password=password)
            return user
        except auth.EmailAlreadyExistsError:
            raise Exception("El email ya está registrado")
        except Exception as e:
            # Para cualquier otro error, lanzamos una excepción general
            raise Exception(f"Error al registrar usuario: {str(e)}")

    # Inicia sesión
    def login_user_auth(self, email, password):
        # URL para la autenticación con email y contraseña de Firebase
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={
            self.api_key}"
        # Preparamos los datos para la solicitud
        datos = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        try:
            response = requests.post(url, json=datos)
            response.raise_for_status()
            # Devolvemos los datos del usuario en formato JSON
            self.user_data = response.json()
            return self.user_data
        except requests.exceptions.HTTPError as e:
            error_message = e.response.json().get('error', {}).get(
                'message', 'Unknown error occurred')
            if error_message == 'EMAIL_NOT_FOUND':
                raise Exception("Email no encontrado")
            elif error_message == 'INVALID_PASSWORD':
                raise Exception("Contraseña no válida")
            else:
                raise Exception(f"Error de autenticación: {error_message}")
        except Exception as e:
            raise Exception(f"Error inesperado: {str(e)}")


    # Genera un enlace para restablecer la contraseña
    def send_password_reset_email(self, email):
        try:  # Genera el enlace para restablecer la contraseña
            reset_link = auth.generate_password_reset_link(
                email)
            return reset_link
        except Exception as e:
            raise Exception(
                f"Error al generar el enlace de recuperación: {str(e)}")

    def get_user_profile(self, uid):
        # Obtenemos los datos del usuario de Firebase Authentication
        try:
            user = auth.get_user(uid)
            ref = db.reference(f'users/{uid}')
            user_data = ref.get() or {}

            return {  # Diccionario con el email y el nombre de usuario
                'email': user.email,
                'display_name': user_data.get('display_name') or user.display_name or 'Usuario'
            }
        except Exception as e:
            raise Exception(
                f"Error al obtener el perfil del usuario: {str(e)}")


    # Actualiza el nombre de usuario en Firebase Authentication
    def update_user_profile(self, uid, display_name=None):
        try:
            auth.update_user(uid, display_name=display_name)
            ref = db.reference(f'users/{uid}')
            ref.update({
                'display_name': display_name
            })
        except Exception as e:
            raise Exception(
                f"Error al actualizar el perfil del usuario: {str(e)}")

    # Cierra la sesión de un usuario
    def logout(self, uid):
        try:
            auth.revoke_refresh_tokens(uid)
            self.user_data = None
        except Exception as e:
            raise Exception(f"Error al cerrar sesión: {str(e)}")
