import flet as ft
from auth import AuthService
import random


class ProfileView(ft.UserControl):
    def __init__(self, auth_service: AuthService, user_data, on_logout):
        super().__init__()
        self.auth_service = auth_service
        self.user_data = user_data
        self.on_logout = on_logout
        self.name_field = None
        self.display_name_text = None
        # Lista de colores para el avatar
        self.avatar_colors = [
            ft.colors.BLUE,
            ft.colors.RED,
            ft.colors.GREEN,
            ft.colors.ORANGE,
            ft.colors.PURPLE,
            ft.colors.PINK,
            ft.colors.TEAL,
            ft.colors.CYAN,
        ]

    def build(self):
        # Obtenemos el perfil del usuario
        user_profile = self.auth_service.get_user_profile(
            self.user_data['localId'])
        # Extraemos el email del usuario
        email = user_profile['email']
        # Obtenemos el nombre de usuario o usamos 'Usuario' por defecto
        display_name = user_profile['display_name']

        # Color aleatorio para el avatar
        avatar_color = random.choice(self.avatar_colors)

        # Determinar la inicial para el avatar
        avatar_initial = (
            display_name[0] if display_name else email[0]).upper()
        # Creamos un avatar simple con las iniciales del usuario
        avatar = ft.Container(
            # Si display_name existe y no está vacío, usa la primera letra de display_name en mayúsculas; de lo contrario, usa la primera letra del email en mayúsculas
            content=ft.Text(avatar_initial, size=32, color=ft.colors.WHITE),
            width=80,
            height=80,
            bgcolor=avatar_color,
            border_radius=40,
            alignment=ft.alignment.center
        )

        # Nombre de usuario y correo
        self.display_name_text = ft.Text(
            display_name, size=24, weight=ft.FontWeight.BOLD)
        email_text = ft.Text(email, size=14, color=ft.colors.GREY_500)

        # Campo de entrada para nuevo nombre
        self.name_field = ft.TextField(
            value=display_name,
            label="Nuevo nombre de usuario",
            width=300
        )

        # Botones
        update_button = ft.ElevatedButton(
            "Actualizar Perfil",
            on_click=self.update_profile,
            width=300
        )
        logout_button = ft.OutlinedButton(
            "Cerrar Sesión",
            on_click=self.logout,
            width=300
        )

        # Devolvemos un Card que contiene todos los elementos de la interfaz
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([avatar], alignment=ft.MainAxisAlignment.CENTER),
                    self.display_name_text,
                    email_text,
                    self.name_field,
                    update_button,
                    logout_button
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
                padding=20,
                width=350
            ),
            elevation=5
        )

    # Método para actualizar el perfil del usuario
    def update_profile(self, _):
        try:
            new_display_name = self.name_field.value
            self.auth_service.update_user_profile(  # Llamamos al servicio de autenticación para actualizar el perfil
                self.user_data['localId'],
                display_name=new_display_name
            )
            self.display_name_text.value = new_display_name
            self.update()
            self.show_notification("Perfil actualizado con éxito")
        except Exception as error:
            self.show_notification(f"Error al actualizar perfil: {str(error)}")

    def show_notification(self, message):
        self.page.snack_bar = ft.SnackBar(content=ft.Text(message))
        self.page.snack_bar.open = True
        self.page.update()

    def logout(self, _):
        if self.on_logout:
            self.on_logout()
