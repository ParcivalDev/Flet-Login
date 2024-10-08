import flet as ft
from login import Login
from registro import Registro


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def cambiar_vista(e):
        c.content = registro.contenedor if c.content == inicio.contenedor else inicio.contenedor
        c.update()

    inicio = Login(cambiar_vista)
    registro = Registro(cambiar_vista)

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
