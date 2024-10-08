import flet as ft


class Registro:
    def __init__(self, on_login_click):
        self.on_login_click = on_login_click  # Primero asignamos on_login_click
        self.contenedor = self.crearContenedor()  # Luego creamos el contenedor
        # Esto es importante porque crearContenedor() utiliza self.on_login_click. Si intentamos crear el contenedor antes de asignar on_login_click, obtendremos un error

    def crearContenedor(self):
        return ft.Container(
            ft.Column([
                ft.Container(
                    ft.Text(
                        "Crear Cuenta",
                        width=320,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_700),
                    padding=ft.padding.only(top=20)),

                ft.Container(
                    ft.TextField(
                        width=250,
                        height=40,
                        hint_text="Correo electrónico",
                        border=ft.InputBorder.UNDERLINE,
                        color=ft.colors.BLACK,  # color del texto
                        prefix_icon=ft.icons.MAIL
                    ), padding=ft.padding.only(top=20)
                ),
                ft.Container(
                    ft.TextField(
                        width=250,
                        height=40,
                        hint_text="Contraseña",
                        border=ft.InputBorder.UNDERLINE,
                        color=ft.colors.BLACK,  # color del texto
                        prefix_icon=ft.icons.PASSWORD,
                        password=True
                    ), padding=ft.padding.only(top=20)
                ),
                ft.Container(
                    ft.TextField(
                        width=250,
                        height=40,
                        hint_text="Repite la contraseña",
                        border=ft.InputBorder.UNDERLINE,
                        color=ft.colors.BLACK,  # color del texto
                        prefix_icon=ft.icons.PASSWORD,
                        password=True
                    ), padding=ft.padding.only(top=20)
                ),
                ft.Container(
                    ft.ElevatedButton(
                        width=230,
                        text="REGISTRARSE",
                        bgcolor=ft.colors.BLACK
                    ),
                    padding=ft.padding.only(top=20)
                ),
                ft.Text("Registrarse con"),
                ft.Container(
                    ft.Row([
                        ft.IconButton(
                            icon=ft.icons.EMAIL,
                            tooltip="Google",
                            icon_size=30,
                            icon_color=ft.colors.RED_700
                        ),
                        ft.IconButton(
                            icon=ft.icons.FACEBOOK,
                            tooltip="Facebook",
                            icon_size=30,
                            icon_color=ft.colors.CYAN_800
                        ),
                        ft.IconButton(
                            icon=ft.icons.APPLE,
                            tooltip="Apple",
                            icon_size=30,
                            icon_color=ft.colors.BLACK
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER
                    )
                ),
                ft.Container(
                    ft.Row([
                        ft.Text("¿Ya tienes cuenta?"),
                        ft.TextButton("Inicia sesión",
                                      on_click=self.on_login_click)
                    ], alignment=ft.MainAxisAlignment.CENTER
                    )
                )

            ], alignment=ft.MainAxisAlignment.SPACE_EVENLY, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=320,
            height=500,
            border_radius=20,
            gradient=ft.LinearGradient([
                ft.colors.RED_400,
                ft.colors.ORANGE_600,
                ft.colors.YELLOW_800
            ])
        )
