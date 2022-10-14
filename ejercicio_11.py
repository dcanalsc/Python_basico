#Enunciado del ejercicio:

#   En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
#   la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que
#   también será de tipo texto.
#   Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#   Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

def main():

    crear_tabla()

    i=0
    while i<8:
        print("Alumno", i +1 )
        crear_alumno(input("Nombre:"), input("Apellido:"))
        i += 1
    print("Buscar alumno:")
    leer_alumno(input())

def crear_tabla():

    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alumnos (id INTEGER, nombre TEXT, apellido TEXT)''')
    conn.commit()                                                   #GRABAMOS RESULTADO
    cursor.close()
    conn.close()


def crear_alumno(nombre, apellido):

    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    valor = cursor.execute('SELECT max(id) FROM Alumnos')           #nos colocamos al final de la tabla
    max_id=valor.fetchone()[0]
    query = '''INSERT INTO Alumnos (id, nombre, apellido) VALUES (?, ?, ?)'''

    if max_id != None: max_id += 1                                  #puntero al final de la tabla para escribir
    else: max_id = 0
    rows = cursor.execute(query, (max_id, nombre, apellido))
    conn.commit()                                                   #GRABAMOS RESULTADO
    cursor.close()
    conn.close()

def leer_alumno(variable):

    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    q = cursor.execute('SELECT id, apellido FROM Alumnos WHERE nombre = ?',(variable,))
    for data in q.fetchall():
        print("Id: %s, Apellido: %s" % (data[0], data[1]))

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()