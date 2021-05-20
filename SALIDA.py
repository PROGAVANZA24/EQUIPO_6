class Salida:


    def __init__(self, fecha, id_objeto, cantidads):
        self.fecha= fecha
        self.id_objeto= id_objeto
        self.cantidads= cantidads

    def fecha_salida(fecha):
        fechas= open("Objetos.txt", "a")
        fecha= input(str("Porfavor, introduzca la fecha de salida: "))
        fechas.write(' fecha=%s' %fecha)
        fechas.close

    def objetoss(id_objetos):
        objetos= open("Objetos.txt","a")
        id_objeto= str(input("Introduzca el id del objeto que desea sacar: "))
        cantidads= int(input("Escriba la cantidad que desea sacar: "))
        print(f'Se a sacado una cantidad de {cantidads} del ID {id_objeto}')
        objetos.write(f' Se saco {cantidads} del Id = {id_objeto}')
        objetos.close

