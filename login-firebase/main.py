import flet as ft
import os
from login import Login
from registro import Registro
from profileview import ProfileView
from auth import initialize_firebase, AuthService


# Función para configurar Firebase
def setup_firebase():
    # Obtenemos la ruta del archivo de configuración de Firebase desde las variables de entorno
    config_path = os.getenv('FIREBASE_CONFIG_PATH')
    if not config_path:
        raise ValueError(
            "FIREBASE_CONFIG_PATH no está configurada en las variables de entorno")
    firebase_app = initialize_firebase(config_path)
    return AuthService(firebase_app)

# Función para mostrar notificaciones en la aplicación
def show_notification(page:ft.Page, message):
    notificacion = ft.SnackBar(content=ft.Text(message))
    page.overlay.append(notificacion)
    notificacion.open = True
    page.update()

def main(page: ft.Page):
    page.title = "Login y Registro con Firebase"
    page.bgcolor = ft.colors.BLACK
    page.window.width = 500
    page.window.center()  # Centrar la ventana en la pantalla
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    auth_service = setup_firebase()

    # Función para cambiar entre diferentes vistas
    def cambiar_vista(vista):
        c.content = vista
        c.update()

    # Función que se ejecuta cuando se inicia sesión
    def handle_login_success(user_data):
        # Creamos una vista de perfil para el usuario que ha iniciado sesión
        profile_view = ProfileView(
            auth_service, user_data, on_logout=handle_logout)
        cambiar_vista(profile_view)
        show_notification(page, f"Inicio de sesión exitoso para {user_data['email']}.")

    # Función que se ejecuta cuando el usuario cierra sesión
    def handle_logout():
        # Volvemos a la vista de inicio de sesión
        cambiar_vista(inicio.contenedor)
        show_notification(page, "Sesión cerrada exitosamente.")

    # Función que se ejecuta cuando el usuario se registra
    def handle_register_success():
        show_notification(page, "Registro exitoso.")
        cambiar_vista(inicio.contenedor)


    # Funciones para cambiar entre las vistas de inicio de sesión y registro
    def to_registro(_):
        cambiar_vista(registro.contenedor)

    def to_inicio(_):
        cambiar_vista(inicio.contenedor)

    # Creamos las instancias de las vistas de inicio de sesión y registro
    inicio = Login(to_registro, auth_service, page)
    registro = Registro(to_inicio, auth_service)

    # Configuramos las funciones para inicio de sesión y registro exitosos
    inicio.on_login_success = handle_login_success
    registro.on_register_success = handle_register_success

    # Creamos un contenedor animado para cambiar entre vistas
    c = ft.AnimatedSwitcher(
        inicio.contenedor,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.EASE
    )

    page.add(c)



ft.app(target=main)
