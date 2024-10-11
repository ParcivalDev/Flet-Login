import flet as ft

# Definimos una clase llamada ProfileView que hereda de ft.UserControl
# Esta clase representa la vista del perfil de usuario en nuestra aplicación


class ProfileView(ft.UserControl):
    def __init__(self, auth_service, user_data, on_logout):
        super().__init__()
        self.auth_service = auth_service
        self.user_data = user_data
        self.on_logout = on_logout
        self.name_field = None
        self.display_name_text = None

    def build(self):
        # Obtenemos el perfil del usuario usando el servicio de autenticación
        user_profile = self.auth_service.get_user_profile(
            self.user_data['localId'])

        # Creamos un texto que muestra el nombre de usuario actual
        self.display_name_text = ft.Text(
            f"Nombre de usuario: {user_profile.get('display_name', 'No establecido')}")

        # Creamos un campo de texto para que el usuario pueda cambiar su nombre
        self.name_field = ft.TextField(value=user_profile.get(
            'display_name', ''), label="Nuevo nombre de usuario")

        # Creamos un botón para actualizar el perfil
        update_button = ft.ElevatedButton(
            "Actualizar perfil", on_click=self.update_profile)

        # Creamos un botón para cerrar sesión
        logout_button = ft.ElevatedButton(
            "Cerrar sesión", on_click=self.logout)

        # Devolvemos una columna con todos los elementos de la interfaz
        return ft.Column([
            ft.Text(f"Email: {self.user_data['email']}",
                    style=ft.TextThemeStyle.BODY_LARGE),
            self.display_name_text,
            self.name_field,
            update_button,
            logout_button
        ])

    def update_profile(self, _):
        try:
            # Obtenemos el nuevo nombre de usuario del campo de texto
            new_display_name = self.name_field.value
            # Actualizamos el perfil del usuario en el servicio de autenticación
            self.auth_service.update_user_profile(
                self.user_data['localId'],
                display_name=new_display_name
            )
            # Actualizamos el texto que muestra el nombre de usuario en la interfaz
            self.display_name_text.value = f"Nombre de usuario: {
                new_display_name}"
            self.update()
            # Mostramos un mensaje de éxito al usuario
            self.show_notification("Perfil actualizado con éxito")
        except Exception as error:
            self.show_notification(f"Error al actualizar perfil: {str(error)}")

    def show_notification(self, message):
        notificacion = ft.SnackBar(content=ft.Text(message))
        self.page.overlay.append(notificacion)
        notificacion.open = True
        self.page.update()

    def logout(self,_):
        if self.on_logout:
            self.on_logout()
