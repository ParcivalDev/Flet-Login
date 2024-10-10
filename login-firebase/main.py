import flet as ft
import os
from login import Login
from registro import Registro
from auth import initialize_firebase, AuthService
from firebase_admin import db


class ProfileView(ft.UserControl):
    def __init__(self, auth_service, user_data, on_logout):
        super().__init__()
        self.auth_service = auth_service
        self.user_data = user_data
        self.on_logout = on_logout
        self.name_field = None
        self.display_name_text = None

    def build(self):
        user_profile = self.auth_service.get_user_profile(
            self.user_data['localId'])

        self.display_name_text = ft.Text(
            f"Nombre de usuario: {user_profile.get('display_name', 'No establecido')}")
        
        self.name_field = ft.TextField(value=user_profile.get(
            'display_name', ''), label="Nuevo nombre de usuario")

        update_button = ft.ElevatedButton(
            "Actualizar perfil", on_click=self.update_profile)
        logout_button = ft.ElevatedButton(
            "Cerrar sesión", on_click=self.logout)

        return ft.Column([
            ft.Text(f"Email: {self.user_data['email']}",
                    style=ft.TextThemeStyle.BODY_LARGE),
            self.display_name_text,
            self.name_field,
            update_button,
            logout_button
        ])

    def update_profile(self, e):
        try:
            new_display_name = self.name_field.value
            self.auth_service.update_user_profile(
                self.user_data['localId'],
                display_name=new_display_name
            )
            self.display_name_text.value = f"Nombre de usuario: {
                new_display_name}"
            self.update()
            self.page.show_snack_bar(ft.SnackBar(
                content=ft.Text("Perfil actualizado con éxito")))
        except Exception as error:
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text(
                f"Error al actualizar perfil: {str(error)}")))

    def logout(self, e):
        if self.on_logout:
            self.on_logout()


def main(page: ft.Page):
    page.title = "Login y Registro con Firebase"
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Inicializar Firebase
    config_path = os.getenv('FIREBASE_CONFIG_PATH')
    if not config_path:
        raise ValueError(
            "FIREBASE_CONFIG_PATH no está configurada en las variables de entorno")

    firebase_app = initialize_firebase(config_path)
    auth_service = AuthService(firebase_app)

    def cambiar_vista(e, vista):
        c.content = vista
        c.update()

    def handle_login_success(user_data):
        profile_view = ProfileView(
            auth_service, user_data, on_logout=handle_logout)
        cambiar_vista(None, profile_view)
        notificacion = ft.SnackBar(content=ft.Text(
            f"Inicio de sesión exitoso para {user_data['email']}."))
        page.show_snack_bar(notificacion)

    def handle_logout():
        cambiar_vista(None, inicio.contenedor)
        notificacion = ft.SnackBar(
            content=ft.Text("Sesión cerrada exitosamente."))
        page.show_snack_bar(notificacion)

    def handle_register_success():
        notificacion = ft.SnackBar(content=ft.Text(f"Registro exitoso."))
        page.show_snack_bar(notificacion)
        cambiar_vista(None, inicio.contenedor)

    inicio = Login(lambda _: cambiar_vista(
        _, registro.contenedor), auth_service, page)
    registro = Registro(lambda _: cambiar_vista(
        _, inicio.contenedor), auth_service)

    inicio.on_login_success = handle_login_success
    registro.on_register_success = handle_register_success

    c = ft.AnimatedSwitcher(
        inicio.contenedor,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.EASE
    )

    page.add(c)


if __name__ == "__main__":
    ft.app(target=main)
