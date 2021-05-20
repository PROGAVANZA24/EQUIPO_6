from ENTRADA import Entrada
from SALIDA import Salida
again= True

while again == True:
    print("Bienvenido")
    print("Este es el menu")
    print("1.- Registrar 1 entrada")
    print("2.- Registrar 1 salida")
    print("3.- Salir")
    print("Porfavor seleccione una opcion")
    respuesta= int(input())

    if respuesta <=0:
        print("Porfavor, seleccione una opcion valida")
    if respuesta >=4:
        print("Porfavor, seleccione una opcion valida")
    if respuesta == 1:
        registrofecha=Entrada.fecha_entrada("")
        registro_objeto=Entrada.objetose("", "", "", "")
    elif respuesta == 2:
        registro_fecha_salida=Salida.fecha_salida("")
        registro_objeto_salida=Salida.objetoss("")
    elif respuesta == 3:
        print ("Gracias por usar nuestro programa")
        again = False


