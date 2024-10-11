import flet as ft


class BaseView:
    def __init__(self, title, switch_text, switch_action, texto):
        self.title = title
        # El texto para cambiar a otra vista. Ej. ¿No tienes cuenta?
        self.switch_text = switch_text
        self.switch_action = switch_action  # La función a ejecutar al cambiar de vista
        self.texto = texto  # El texto del botón para cambiar de vista. Ej. Regístrate
        self.message = ft.Text()  # Texto para mostrar mensajes al usuario
        self.contenedor = self.crear_contenedor()

    # Crea el contenedor principal de la vista

    def crear_contenedor(self):
        return ft.Container(
            ft.Column([
                self.crear_titulo(),
                self.crear_campos(),
                self.crear_boton_principal(),
                self.crear_opciones(),
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
        pass

    def crear_boton_principal(self):
        pass

    def crear_opciones(self):
        return ft.Container(
            ft.Row([
                ft.IconButton(icon=ft.icons.EMAIL, tooltip="Google",
                              icon_size=30, icon_color=ft.colors.RED_700),
                ft.IconButton(icon=ft.icons.FACEBOOK, tooltip="Facebook",
                              icon_size=30, icon_color=ft.colors.CYAN_800),
                ft.IconButton(icon=ft.icons.APPLE, tooltip="Apple",
                              icon_size=30, icon_color=ft.colors.BLACK)
            ], alignment=ft.MainAxisAlignment.CENTER)
        )

    def crear_switch_view(self):
        return ft.Container(
            ft.Row([
                ft.Text(self.switch_text),
                ft.TextButton(text=self.texto, on_click=self.switch_action, style=ft.ButtonStyle(
                    color={
                        ft.ControlState.DEFAULT: ft.colors.CYAN_700,
                        ft.ControlState.HOVERED: ft.colors.CYAN_300,
                        ft.ControlState.FOCUSED: ft.colors.GREEN,
                        ft.ControlState.PRESSED: ft.colors.RED,
                    },
                    animation_duration=300
                ))
            ], alignment=ft.MainAxisAlignment.CENTER)
        )

    def crear_campo(self, hint, icon, password=False, can_reveal_password=False):
        return ft.Container(
            ft.TextField(
                width=250,
                height=40,
                hint_text=hint,
                border=ft.InputBorder.UNDERLINE,
                color=ft.colors.BLACK,
                prefix_icon=icon,
                password=password,
                can_reveal_password=can_reveal_password
            ),
            padding=ft.padding.only(top=20)
        )

    def crear_boton(self, text, on_click, width=230):
        return ft.Container(
            ft.ElevatedButton(
                width=width,
                text=text,
                bgcolor=ft.colors.BLACK,
                on_click=on_click
            ),
            padding=ft.padding.only(top=20)
        )

    def mostrar_mensaje(self, mensaje, es_error=True):
        self.message.value = mensaje
        self.message.color = ft.colors.RED if es_error else ft.colors.GREEN
        self.message.update()

    def mostrar_error(self, mensaje):
        self.mostrar_mensaje(mensaje, es_error=True)

    def mostrar_exito(self, mensaje):
        self.mostrar_mensaje(mensaje, es_error=False)
