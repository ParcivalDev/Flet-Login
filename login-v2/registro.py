import flet as ft
from base import BaseView


class Registro(BaseView):
    def __init__(self, on_login_click):
        super().__init__("Crear Cuenta", "¿Ya tienes cuenta?", on_login_click, "Registrarse")

    def crear_campos(self):
        return ft.Column([
            self.crear_campo("Correo electrónico", ft.icons.MAIL),
            self.crear_campo("Contraseña", ft.icons.PASSWORD, password=True),
            self.crear_campo("Repite la contraseña",
                             ft.icons.PASSWORD, password=True)
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
                              bgcolor=ft.colors.BLACK),
            padding=ft.padding.only(top=20)
        )
