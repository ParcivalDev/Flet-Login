import flet as ft
from base import BaseView
import re

class Registro(BaseView):
    def __init__(self, on_login_click, auth_service):
        super().__init__("Crear Cuenta", "¿Ya tienes cuenta?",
                         on_login_click, "Inicia sesión")
        self.auth_service = auth_service
        self.on_register_success = None

    def crear_campos(self):
        self.email_field = self.crear_campo(
            "Correo electrónico", ft.icons.MAIL)
        self.password_field = self.crear_campo(
            "Contraseña", ft.icons.PASSWORD, password=True)
        self.confirm_password_field = self.crear_campo(
            "Repite la contraseña", ft.icons.PASSWORD, password=True)
        return ft.Column([
            self.email_field,
            self.password_field,
            self.confirm_password_field,
            self.message
        ])

    def crear_boton_principal(self):
        return self.crear_boton("REGISTRARSE", self.register_user)

    def register_user(self, e):
        email = self.email_field.content.value
        password = self.password_field.content.value
        confirm_password = self.confirm_password_field.content.value

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

        try:
            user = self.auth_service.register_user(email, password)
            self.mostrar_exito(f"Usuario registrado exitosamente: {user.uid}")
            if self.on_register_success:
                self.on_register_success()
        except Exception as error:
            self.mostrar_error(f"Error de registro: {str(error)}")

    def validar_email(self, email):
        # Implementamos una validación de email usando expresiones regulares
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None