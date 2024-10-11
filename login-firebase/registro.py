import flet as ft
from base import BaseView
import re  # Biblioteca para trabajar con expresiones regulares
from auth import AuthService


class Registro(BaseView):  # Clase Registro que hereda de BaseView
    def __init__(self, on_login_click, auth_service):
        super().__init__("Crear Cuenta", "¿Ya tienes cuenta?",
                         on_login_click, "Inicia sesión")
        self.auth_service: AuthService = auth_service
        self.on_register_success = None

    def crear_campos(self):
        self.email_field = self.crear_campo(
            "Correo electrónico", ft.icons.MAIL)
        self.password_field = self.crear_campo(
            "Contraseña", ft.icons.PASSWORD, password=True, can_reveal_password=True)
        self.confirm_password_field = self.crear_campo(
            "Repite la contraseña", ft.icons.PASSWORD, password=True, can_reveal_password=True)
        return ft.Column([
            self.email_field,
            self.password_field,
            self.confirm_password_field,
            self.message
        ])

    def crear_boton_principal(self):
        return self.crear_boton("REGISTRARSE", self.register_user)

    # Método para obtener el valor de los campos de texto
    # Espera un parámetro container que contiene un TextField
    # email_field es un contenedor con un TextField

    def get_field_value(self, field: ft.Container):
        return field.content.value if isinstance(field.content, ft.TextField) else ""

    def register_user(self, _):
        # Obtenemos los valores ingresados por el usuario
        email = self.get_field_value(self.email_field)
        password = self.get_field_value(self.password_field)
        confirm_password = self.get_field_value(self.confirm_password_field)

        if password != confirm_password:
            self.mostrar_error("Las contraseñas no coinciden")
            return

        if not self.validar_email(email):
            self.mostrar_error("Email inválido")
            return

        if len(password) < 6:
            self.mostrar_error(
                "La contraseña debe tener al menos 6 caracteres")
            return

        # Si todas las validaciones pasan, intentamos registrar al usuario
        try:
            user = self.auth_service.register_user(email, password)
            user_id = user.get('uid') if isinstance(
                user, dict) else getattr(user, 'uid', 'ID no disponible')
            self.mostrar_exito(f"Usuario registrado exitosamente: {user_id}")
            if self.on_register_success:  # Esto es verdadero porque contiene handle_register_success
                self.on_register_success()  # Esto ejecuta handle_register_success
        except Exception as error:
            self.mostrar_error(f"Error de registro: {str(error)}")

    def validar_email(self, email):
        # Implementamos una validación de email más robusta
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
