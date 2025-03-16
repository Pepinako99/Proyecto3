import flet as ft
import ddbb

def main(page: ft.Page):
    page.title = "Consultas"

    # Consultar y cargar todos los arboles
    def consultar_usuarios():
        usuarios = ddbb.consultar_usuarios() # Estos son los datos
        cargar_tabla(usuarios)
        page.update()

    # Datos es la lista de arboles
    def cargar_tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))), # ID
                ft.DataCell(ft.Text(fila[1])),
                ft.DataCell(ft.Text(fila[2])),
                ft.DataCell(ft.Text(str(fila[3]))),
                ft.DataCell(ft.Text(str(fila[4]))),
                ft.DataCell(ft.Text(str(fila[5]))),
            ]))

    def buscar_usuarios(e):
        lista_usuarios = ddbb.consultar_usuarios_por_nombre(nombre_tf.value)
        cargar_tabla(lista_usuarios)
        page.update()

    def volver(e):
        page.go("/formulario")

    # OBJETOS
    nombre_tf = ft.TextField(label="Nombre", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", on_click=buscar_usuarios , width=300)
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)
    tabla = ft.DataTable(bgcolor="blue",
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Contraseña")),
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Ultimo Login")),
        ]
    )
    columna_datos = ft.Column(
        controls=[
            ft.Text("CONSULTAS", size=40),
            nombre_tf,
            buscar_btn,
            tabla,
            volver_btn,

        ]
    )

    #page.add(columna_datos)
    consultar_usuarios()

    return columna_datos



