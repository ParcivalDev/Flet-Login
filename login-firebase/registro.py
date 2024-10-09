import flet as ft
from base import BaseView

class Registro(BaseView):
    def __init__(self, on_login_click, auth_service):
        self.message = ft.Text()  # Para mostrar mensajes de error o éxito
        super().__init__("Crear Cuenta", "¿Ya tienes cuenta?",
                         on_login_click, "Inicia sesión")
        self.auth_service = auth_service
        

    def crear_campos(self):
        self.email_field = self.crear_campo("Correo electrónico", ft.icons.MAIL)
        self.password_field = self.crear_campo("Contraseña", ft.icons.PASSWORD, password=True)
        self.confirm_password_field = self.crear_campo("Repite la contraseña", ft.icons.PASSWORD, password=True)
        return ft.Column([
            self.email_field,
            self.password_field,
            self.confirm_password_field,
            self.message  # Añadimos el campo de mensaje aquí
        ])

    def crear_campo(self, hint, icon, password=False):
        return ft.Container(
            ft.TextField(
                width=250,
                height=40,
                hint_text=hint,
                border=ft.InputBorder.UNDERLINE,
                color=ft.colors.BLACK,
                prefix_icon=icon,
                password=password
            ),
            padding=ft.padding.only(top=20)
        )

    def crear_boton_principal(self):
        return ft.Container(
            ft.ElevatedButton(width=230, text="REGISTRARSE",
                              bgcolor=ft.colors.BLACK, on_click=self.register_user),
            padding=ft.padding.only(top=20)
        )

    def register_user(self, e):
        email = self.email_field.content.value
        password = self.password_field.content.value
        confirm_password = self.confirm_password_field.content.value

        if password != confirm_password:
            self.mostrar_error("Las contraseñas no coinciden")
            return

        try:
            if self.on_register_success:
                self.on_register_success()
        except Exception as error:
            self.mostrar_error(f"Error de registro: {str(error)}")
            

    def mostrar_error(self, mensaje):
        self.message.value = mensaje
        self.message.color = ft.colors.RED
        self.message.update()

    def mostrar_exito(self, mensaje):
        self.message.value = mensaje
        self.message.color = ft.colors.GREEN
        self.message.update()