import os
import flet as ft
from dotenv import load_dotenv
from login import Login
from registro import Registro
from auth import initialize_firebase, AuthService

# Cargar variables de entorno
load_dotenv()

def main(page: ft.Page):
    page.title = "Login y Registro con Firebase"
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Inicializar Firebase
    config_path = os.getenv('FIREBASE_CONFIG_PATH')
    if not config_path:
        raise ValueError("FIREBASE_CONFIG_PATH no está configurada en las variables de entorno")
    
    firebase_app = initialize_firebase(config_path)
    auth_service = AuthService(firebase_app)

    # Función para cambiar entre las vistas de login y registro
    def cambiar_vista(e):
        c.content = registro.contenedor if c.content == inicio.contenedor else inicio.contenedor
        c.update()

    # Función para manejar el inicio de sesión exitoso
    def handle_login_success():
        notificacion = ft.SnackBar(content=ft.Text(f"Inicio de sesión exitoso."))
        page.overlay.append(notificacion)
        notificacion.open = True
        page.update()

    # Función para manejar el registro exitoso
    def handle_register_success():
        notificacion = ft.SnackBar(content=ft.Text(f"Registro exitoso."))
        page.overlay.append(notificacion)
        notificacion.open = True
        page.update()
        cambiar_vista(None)  # Cambia a la vista de inicio de sesión

    # Crear instancias de Login y Registro
    inicio = Login(cambiar_vista, auth_service)
    registro = Registro(cambiar_vista, auth_service)

    # Asignar las funciones de manejo a las instancias de Login y Registro
    inicio.on_login_success = handle_login_success
    registro.on_register_success = handle_register_success

    # Crear un contenedor animado para cambiar entre vistas
    c = ft.AnimatedSwitcher(
        inicio.contenedor,  # Contenido inicial
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.EASE
    )

    # Añadir el contenedor a la página
    page.add(c)

if __name__ == "__main__":
    ft.app(target=main)