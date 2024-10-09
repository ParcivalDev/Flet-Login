import flet as ft
from base import BaseView


class Login(BaseView):
    def __init__(self, on_register_click, auth_service):
        self.message = ft.Text()  # Inicializamos el atributo message aquí

        super().__init__("Iniciar sesión", "¿No tienes cuenta?",
                         on_register_click, "Regístrate")
        self.auth_service = auth_service
        self.on_login_success = None  # Callback para el éxito de inicio de sesión

    def crear_campos(self):
        self.email_field = self.crear_campo(
            "Correo electrónico", ft.icons.MAIL)
        self.password_field = self.crear_campo(
            "Contraseña", ft.icons.PASSWORD, password=True)

        return ft.Column([
            self.email_field,
            self.password_field,
            ft.Container(
                ft.Checkbox(label="Recordar contraseña",
                            check_color=ft.colors.BLUE),
                padding=ft.padding.only(80)
            ),
            self.message  # Añadimos el campo de mensaje aquí
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

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
            padding=ft.padding.only(top=20),
        )

    def crear_boton_principal(self):
        return ft.Container(
            ft.ElevatedButton(width=230, text="INICIAR",
                              bgcolor=ft.colors.BLACK, on_click=self.login_user),
            padding=ft.padding.only(top=20)
        )

    def login_user(self, e):
        try:
            user = self.auth_service.login_user(
                self.email_field.content.value, self.password_field.content.value)
            if self.on_login_success:
                self.on_login_success()
        except Exception as error:
            self.mostrar_error(str(error))

    def mostrar_error(self, mensaje):
        self.message.value = mensaje
        self.message.color = ft.colors.RED
        self.message.update()

    def mostrar_exito(self, mensaje):
        self.message.value = mensaje
        self.message.color = ft.colors.GREEN
        self.message.update()
