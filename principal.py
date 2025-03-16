import flet as ft
import formularioPage
import consultaPage

def main(page: ft.Page):
    page.title = "APP USUARIOS"

    def route_change(e):
        page.views.clear()
        if page.route == "/formulario":
            page.views.append(
                ft.View(
                    route = "/formulario",
                    controls = [formularioPage.main(page)]
                )
            )
        elif page.route == "/consultas":
            page.views.append(
                ft.View(
                    route="/consultas",
                    controls=[consultaPage.main(page)]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/formulario")

if __name__ == '__main__':
    ft.app(target=main)

#cambio