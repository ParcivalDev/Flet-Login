import flet as ft
from base import BaseView


class Login(BaseView):
    def __init__(self, on_register_click):
        super().__init__("Iniciar sesión", "¿No tienes cuenta?",
                         on_register_click, "Iniciar sesión")

    def crear_campos(self):
        return ft.Column([
            self.crear_campo("Correo electrónico", ft.icons.MAIL),
            self.crear_campo("Contraseña", ft.icons.PASSWORD, password=True),
            ft.Container(
                ft.Checkbox(label="Recordar contraseña",
                            check_color=ft.colors.BLUE),
                padding=ft.padding.only(80)
            )
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER)

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
                              bgcolor=ft.colors.BLACK),
            padding=ft.padding.only(top=20)
        )
