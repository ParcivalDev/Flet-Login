import flet as ft


class Login:
    def __init__(self, on_register_click):
        self.on_register_click = on_register_click
        self.contenedor = self.crearContenedor()

    def crearContenedor(self):
        return ft.Container(
            ft.Column([
                ft.Container(
                    ft.Text(
                        "Iniciar sesión",
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
                    ft.Checkbox(
                        label="Recordar contraseña",
                        check_color=ft.colors.BLUE,

                    ),
                    padding=ft.padding.only(80)
                ),
                ft.Container(
                    ft.ElevatedButton(
                        width=230,
                        text="INICIAR",
                        bgcolor=ft.colors.BLACK
                    ),
                    padding=ft.padding.only(top=20)
                ),
                ft.Text("Iniciar sesión con"),
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
                        ft.Text("¿No tienes cuenta?"),
                        ft.TextButton("Regístrate", on_click= self.on_register_click)
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
