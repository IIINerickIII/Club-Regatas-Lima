import os

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
        
