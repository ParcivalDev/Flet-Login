import flet as ft
from registro import Registro
from login import Login


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def cambiar_a_registro(e):
        c.content = registro.contenedor
        c.update()

    def cambiar_a_login(e):
        c.content = inicio.contenedor
        c.update()

    registro = Registro(on_login_click=cambiar_a_login)
    inicio = Login(on_register_click=cambiar_a_registro)

    c = ft.AnimatedSwitcher(
        inicio.contenedor,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.EASE
    )

    page.add(c)


ft.app(main)
