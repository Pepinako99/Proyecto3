import psycopg2

def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="proyecto",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    return conn

def consultar_usuarios_por_nombre(nombre):
    conn = connect()
    usuarios = []
    try:
        cursor = conn.cursor()
        query = """
                SELECT * 
                FROM usuarios
                WHERE lower(nombre) = lower(%s);
                """
        cursor.execute(query, (nombre,))
        usuarios = cursor.fetchall()

    except Exception as e:
        print(f"Error al obtener los usuarios {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    print(usuarios)
    return usuarios

def consultar_usuarios():
    conn = connect()
    usuarios = []
    try:
        cursor = conn.cursor()
        query = """
                SELECT * 
                FROM usuarios;
                """
        cursor.execute(query)
        usuarios = cursor.fetchall()

    except Exception as e:
        print(f"Error al obtener los usuarios {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    print(usuarios)
    return usuarios


def insertar_usuarios(nombre, email, contrasena, fecha , fecha_actual):
    """
    Inserta un nuevo árbol en la base de datos.

    Parámetros:
    - nombre (str): Nombre del árbol (ejemplo: "Pino").
    - tipo (str): Puede ser "Perenne" o "Caduca".
    - altura_promedio (int): Altura promedio del árbol en metros.
    - fecha_plantacion (str): Fecha en formato 'YYYY-MM-DD' de la plantación.
    """
    conn = connect()  # Conectar a la base de datos
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar consultas SQL

        # Consulta SQL para insertar un nuevo árbol en la tabla 'Arboles'
        query = """
        INSERT INTO usuarios (nombre, email, contrasena, fecha, ultimo_login)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (nombre, email, contrasena, fecha ,fecha_actual))

        # Confirmar la transacción
        conn.commit()
        print("Usuario registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos

# Ejemplo de uso:
# insertar_arbol("Pino", "Perenne", 30, "2005-03-15")
consultar_usuarios()