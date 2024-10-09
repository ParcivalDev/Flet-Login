import firebase_admin
import os
from firebase_admin import credentials, auth
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def initialize_firebase(config_path):
    """Inicializa la aplicación Firebase."""
    cred = credentials.Certificate(config_path)
    return firebase_admin.initialize_app(cred)

class AuthService:
    def __init__(self, firebase_app):
        self.firebase_app = firebase_app
        self.api_key = os.getenv("FIREBASE_API_KEY")
        if not self.api_key:
            raise ValueError("FIREBASE_API_KEY no está configurada en las variables de entorno")

    def register_user(self, email, password):
        """Registra un nuevo usuario en Firebase."""
        try:
            user = auth.create_user(email=email, password=password)
            return user
        except auth.EmailAlreadyExistsError:
            raise Exception("El email ya está registrado")
        except Exception as e:
            raise Exception(f"Error al registrar usuario: {str(e)}")

    def login_user(self, email, password):
        """Inicia sesión de un usuario usando la API REST de Firebase."""
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            error_message = e.response.json().get('error', {}).get('message', 'Unknown error occurred')
            if error_message == 'EMAIL_NOT_FOUND':
                raise Exception("Email no encontrado")
            elif error_message == 'INVALID_PASSWORD':
                raise Exception("Contraseña inválida")
            else:
                raise Exception(f"Error de autenticación: {error_message}")
        except Exception as e:
            raise Exception(f"Error inesperado: {str(e)}")
