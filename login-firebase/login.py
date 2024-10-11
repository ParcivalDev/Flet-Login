import flet as ft
from base import BaseView
from auth import AuthService

class Login(BaseView):
    def __init__(self, on_register_click, auth_service, page):
        super().__init__("Iniciar sesión", "¿No tienes cuenta?",
                         on_register_click, "Regístrate")
        self.auth_service: AuthService = auth_service
        self.page = page
        self.on_login_success = None

        

    # Crea los campos de entrada para el inicio de sesión

    def crear_campos(self):
        self.email_field = self.crear_campo(
            "Correo electrónico", ft.icons.MAIL)
        self.password_field = self.crear_campo(
            "Contraseña", ft.icons.PASSWORD, password=True, can_reveal_password=True)
        self.forgot_password_button = ft.TextButton(
            text="Olvidé mi contraseña",
            on_click=self.send_password_reset_email
        )

        return ft.Column([
            self.email_field,
            self.password_field,
            self.forgot_password_button,
            self.message
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # Crea el botón principal de inicio de sesión
    # Devuelve un contenedor con el botón de inicio de sesión
    def crear_boton_principal(self):
        return self.crear_boton("INICIAR", self.login_user)

    # Método para obtener el valor de los campos de texto
    # Espera un parámetro container que contiene un TextField
    # email_field es un contenedor con un TextField
    def get_field_value(self, field: ft.Container):
        return field.content.value if isinstance(field.content, ft.TextField) else ""
    
    #  Maneja el proceso de inicio de sesión del usuario
    def login_user(self, _):
        try:
            user = self.auth_service.login_user_auth(
                self.get_field_value(self.email_field),
                self.get_field_value(self.password_field))
            if self.on_login_success:
                self.on_login_success(user)
        except Exception as error:
            self.mostrar_error(str(error))

    # Abre una ventana para recuperar la contraseña
    def send_password_reset_email(self, _):
        email = self.get_field_value(self.email_field)
        if not email:
            self.mostrar_error("Por favor, ingrese su correo electrónico")
            return  # Para salir de la función
        try:
            reset_link = self.auth_service.send_password_reset_email(email)
            self.page.launch_url(reset_link)
            self.mostrar_exito(
                "Se ha abierto una ventana para restablecer su contraseña")
        except Exception as error:
            self.mostrar_error(f"Error: {str(error)}")
