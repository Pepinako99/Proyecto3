import datetime

import ddbb
import flet as ft





def main(page : ft.Page):
    page.title = "CONTROL USUARIOS"

    def abrir_selector(e):
        date_picker.open = True
        page.update()

    def seleccionar_fecha(e):
        fecha_txt.value = f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}"
        page.update()


    def crear_usuarios(e):
        nombre = nombre_tf.value
        email = email_ft.value
        contrasena = contrasena_ft.value
        fecha = date_picker.value
        fecha_actual = datetime.date.today()
        ddbb.insertar_usuarios(nombre, email, contrasena, fecha , fecha_actual)

    def volver(e):
        page.go("/consultas")

    # OBJETOS
    nombre_tf = ft.TextField(label="Nombre", width=300)
    email_ft = ft.TextField(label="Email", width=300)
    contrasena_ft = ft.TextField(label="Contraseña", width=300)

    date_picker = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())
    fecha_txt = ft.Text(f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}")
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)

    columna_datos = ft.Column(
        controls=[ft.Text("USUARIOS", size=40),
                  nombre_tf,
                  email_ft,
                  contrasena_ft,
                  fecha_txt,
                  ft.FilledButton("SELECCIONAR FECHA", on_click=abrir_selector),
                  ft.FilledButton("CREAR USUARIO", on_click=crear_usuarios),
                  volver_btn,
                  ],
    )

    page.overlay.append(date_picker)
    #page.add(columna_datos)
    return columna_datos

#cambiooo