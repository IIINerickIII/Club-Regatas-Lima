import os
import sqlite3
import datetime


def tabla():
    
    conexion=sqlite3.connect("club.sqlite")
    consulta=conexion.cursor()
    tabla="CREATE TABLE IF NOT EXISTS club (Nro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, DNI INTEGER NOT NULL, Nombre TEXT NOT NULL, Apellido TEXT NOT NULL, Deporte TEXT NOT NULL, Edad INTEGER NOT NULL, Sexo TEXT NOT NULL, Profesion TEXT NOT NULL, Ingresos FLOAT NOT NULL, Fecha DATE NOT NULL, Direccion TEXT NOT NULL, Numero INTEGER NOT NULL)"
    if consulta.execute(tabla):
        print("\ttabla creada con exito")
    else:
        print("\tA ocurrido un error al crear una tabla")
    consulta.close()
    conexion.commit()
    conexion.close()

def datos():
    
    while True:
        DNI = str(input('\tIngrese su DNI:\t'))
        if len(DNI) == 8 and not(DNI.isalpha()):
            print('\tDNI valido')
            break
        else:
            print('\tDNI Incorrecto')
    while True:
        Nombre = input('\tIngrese sus Nombres:\t')
        if Nombre.istitle():
            Nombre = str(Nombre)
            print('\tNombre valido')
            break
        else:
            print('\tIncorrecto')
    while True:
        Apellido = input('\tIngrese sus Apellidos:\t')
        if Apellido.istitle():
            Apellido = str(Apellido)
            print('\tApellido Valido')
            break
        else:
            print('\tIncorrecto')
    while True:
        Deporte = input('\tIngrese el Nombre del Deporte que practica:\t')
        if Deporte.isalpha():
            Deporte = str(Deporte)
            print('\tCorrecto')
            break
        else:
            print('\tIncorrecto')
    while True:
        Sexo = input('\tIngrese su sexo: \n\tMasculino (M)\n\tFemenino (F):\t')
        if Sexo.isalpha():
            Sexo = str(Sexo)
            print('\tCorrecto')
            break
        else:
            print('\tIncorrecto')
    while True:
        Profesion = input('\tIngrese la Profesion que Ejerce en la actualidad:\t')
        if Profesion.istitle():
            Profesion = str(Profesion)
            print('\tCorrecto')
            break
        else:
            print('\tIncorrecto')
    while True:
        Ingresos = input('\tIngrese su Remuneracion Mensual:\t')
        if Ingresos.isdigit():
            Ingresos = float(Ingresos)
            print('\tCorrecto')
            break
        else:
            print('\tIncorrecto')
    while True:
        Direccion = input('\tIngrese la Direccion de su Domicilio:\t')
        if Direccion.istitle():
            Direccion = str(Direccion)
            print('\tCorrecto')
            break
        else:
            print('\tIncorrecto')
    while True:
        Numero = input('\tIngrese su numero de Telefono o Celular:\t')
        if Numero.isdigit():
            Numero = int(Numero)
            print('\tNumero Correcto')
            break
        else:
            print('\tIncorrecto')
    while True:
        Edad = int(input('\tIngrese su Edad:\t'))
        if Edad >= 18 and Edad <= 100:
            print('\tCorrecto, usted es mayor de edad')
            break
        else:
            print('\tEdad no valida')

    conexion=sqlite3.connect("club.sqlite")
    consulta=conexion.cursor()
    argumentos=(DNI,Nombre,Apellido,Deporte,Edad,Sexo,Profesion,Ingresos,datetime.date.today(),Direccion,Numero)
    variable="INSERT INTO club (DNI,Nombre,Apellido,Deporte,Edad,Sexo,Profesion,Ingresos,Fecha,Direccion,Numero) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
    if (consulta.execute(variable,argumentos)):
        print("Registro guardado con exito")
    else:
        print("A ocurrido un error al guardar los datos")
    consulta.close()
    conexion.commit()
    conexion.close()
    
def mostrar():
    conexion=sqlite3.connect("club.sqlite")
    consulta=conexion.cursor()
    consulta.execute('SELECT * FROM club')
    for row in consulta:
        print(row)
    consulta.close()
    conexion.close()

def limpiar():
    y = input('\tIngrese el numero de DNI que desee eliminar:\t')
    conexion=sqlite3.connect("club.sqlite")
    y='DELETE FROM club WHERE DNI='+str(y)
    borrar=y
    conexion.execute(borrar)
    conexion.commit()
    conexion.close()

print('''
\t\t\t\tCLUB DE REGATAS LIMA

\t\t\tAv. Chachi Dibós 1201 - Chorrillos



El Club de Regatas Lima fue fundado el 26 de abril de 1875 en el distrito de Chorrillos,
provincia y departamento de Lima, Perú. Por iniciativa de Vicente Oyague y Soyer, junto
a cuatro amigos: Francisco Pérez de Velasco, Domingo García, Francisco Rivera y Enrique
Pérez de Velasco. Ellos se unieron para practicar el remo, deporte que Oyague y Soyer había
disfrutado durante sus años de estudiante en Inglaterra. En un inicio, el Regatas se dedicó
exclusivamente a la práctica de este deporte; debido a eso, nuestro escudo, muestra dos
remos cruzados.

\t\t\t\t\tPRESIDENTE: Gustavo Fernando Salazar Delgado
\t\t\t\t\t\t\t\t2016 – 2018


\t\t\tTELEFONO: 2134567/985641402




''')

y=input("PRESIONE ENTER PARA CONTINUAR\t")
if y=='GHGHGHFGFG':
    print("Usted saldra del programa")
else:
    os.system("cls")
    opcion = 's'
    while opcion in 'sS':
        print ('''
    \t\tMENU
    \t1.- Crear tabla
    \t2.- Insertar datos
    \t3.- Mostrar Datos
    \t4.- Modificar Datos
    \t5.- Eliminar Datos
    \t6.- Salir
    ''')
        opcion=input('\tElija una Opcion:\t')
        if opcion == '1':
            tabla()
        elif opcion == '2':
            datos()
        elif opcion == '3':
            mostrar()
        elif opcion == '4':
            print('falta lo del manuelodaskfhasdlkjfhklasdjfhlkasdjfhlfasdkjhlkasdjhfklfsj')
        elif opcion == '5':
            limpiar()
        elif opcion == '6':
            break
        opcion = input('\tPresione s para continuar, si no cualquier tecla para salir:\t')
        
