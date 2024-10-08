import flet as ft


class BaseView:
    def __init__(self, title, switch_text, switch_action, texto):
        self.title = title
        self.switch_text = switch_text
        self.switch_action = switch_action
        self.texto = texto
        self.contenedor = self.crear_contenedor()

    def crear_contenedor(self):
        return ft.Container(
            ft.Column([
                self.crear_titulo(),
                self.crear_campos(),
                self.crear_boton_principal(),
                self.crear_opciones_login(),
                self.crear_switch_view()
            ], alignment=ft.MainAxisAlignment.SPACE_EVENLY, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=320,
            height=500,
            border_radius=20,
            gradient=ft.LinearGradient(
                [ft.colors.RED_400, ft.colors.ORANGE_600, ft.colors.YELLOW_800])
        )

    def crear_titulo(self):
        return ft.Container(
            ft.Text(self.title, width=320, size=30,
                    text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_700),
            padding=ft.padding.only(top=20)
        )

    def crear_campos(self):
        # Este método debe ser implementado por las clases hijas
        pass

    def crear_boton_principal(self):
        # Este método debe ser implementado por las clases hijas
        pass

    def crear_opciones_login(self):
        return ft.Column([
            ft.Text(f"{self.texto} con"),
            ft.Container(
                ft.Row([
                    ft.IconButton(icon=ft.icons.EMAIL, tooltip="Google",
                                  icon_size=30, icon_color=ft.colors.RED_700),
                    ft.IconButton(icon=ft.icons.FACEBOOK, tooltip="Facebook",
                                  icon_size=30, icon_color=ft.colors.CYAN_800),
                    ft.IconButton(icon=ft.icons.APPLE, tooltip="Apple",
                                  icon_size=30, icon_color=ft.colors.BLACK)
                ], alignment=ft.MainAxisAlignment.CENTER)
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def crear_switch_view(self):
        return ft.Container(
            ft.Row([
                ft.Text(self.switch_text),
                ft.TextButton(self.title, on_click=self.switch_action)
            ], alignment=ft.MainAxisAlignment.CENTER)
        )
