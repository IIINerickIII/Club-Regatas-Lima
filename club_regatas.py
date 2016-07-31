import os
import sqlite3

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
    
    DNI = str(input('Ingrese su DNI: '))
    Nombre = input('Nombre: ')
    Apellido=input("Ingrese sus apellidos:\t")
    Deporte=input("Ingrese su deporte que prefiere:\t")
    Edad=input("Ingrese su edad:\t")
    Sexo=input("Ingrese M si usted es masculino y F si usted es femenino:\t")
    Profesion=input("Ingrese la profesion que ejerce en la actualidad:\t")
    Ingresos=input("Ingrese remuneracion mensual:\t")
    Direccion=input("Ingrese su direccion de su domicilio:\t")
    Numero=input("Ingrese su numero telefonico:\t")

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
    for ver in consulta.execute("SELECT*FROM club"):
        if len(str(ver[1]))>7:
            ver=str(ver[1])+'\t'+str(ver[2])+'\t'+str(ver[3])+'\t'+str(ver[4])+'\t'+str(ver[5])+'\t'+str(ver[6])+'\t'+str(ver[7])+'\t'+str(ver[8])+'\t'+str(ver[9])+'\t'+str(ver[10])+'\t'+str(ver[11])
        else:
            ver=str(ver[1])+'\t\t'+str(ver[2])+'\t\t'+str(ver[3])+'\t\t'+str(ver[4])+'\t\t'+str(ver[5])+'\t\t'+str(ver[6])+'\t\t'+str(ver[7])+'\t\t'+str(ver[8])+'\t\t'+str(ver[9])+'\t\t'+str(ver[10])+'\t\t'+str(ver[11])

    print(ver)
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
        
