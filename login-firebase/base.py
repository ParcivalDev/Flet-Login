import flet as ft


class BaseView:
    def __init__(self, title, switch_text, switch_action, texto):
        self.title = title  # Título de la vista
        self.switch_text = switch_text  # Texto para cambiar entre vistas
        self.switch_action = switch_action  # Función para cambiar entre vistas
        # Texto adicional (para "Iniciar sesión con" o "Registrarse con")
        self.texto = texto
        # Crea el contenedor principal de la vista
        self.contenedor = self.crear_contenedor()

    def crear_contenedor(self):
        return ft.Container(
            ft.Column([  # Columna principal que contiene todos los elementos de la vista
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
        return ft.Container(  # Contiene el título que se añade en login o registro
            ft.Text(self.title, width=320, size=30,
                    text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_700),
            padding=ft.padding.only(top=20)
        )

    # Métodos abstractos que deben ser implementados por las subclases
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
        

    # Método para crear el botón de cambio de vista
    def crear_switch_view(self):
        return ft.Container(
            ft.Row([
                ft.Text(self.switch_text),
                # ft.TextButton(
                #     content=ft.Text(
                #         self.title,
                #         color=ft.colors.BLUE,
                #         weight=ft.FontWeight.W_600,
                #         font_family= "ROBOTO"
                #     ),
                #     on_click=self.switch_action,
                # )
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
