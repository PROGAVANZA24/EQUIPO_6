class Entrada:
    def __init__(self, fecha, objeto, cantidad, precio, id_objeto):
        self.objeto= objeto
        self.cantidad= cantidad
        self.id_objeto= id_objeto
        self.fecha= fecha
        self.precio= precio

    def fecha_entrada(fecha):
        fechae= open("Objetos.txt", "a")
        fecha= input(str("Porfavor, introduzca la fecha de entrada: "))
        fechae.write('fecha=%s' %fecha)
        fechae.close

    def objetose(id_objeto, objeto, cantidad, precio):
        objetos= open("Objetos.txt","a")
        objeto= str(input("Porfavor, Introdusca el objeto que desea agregar: "))
        cantidad= int(input("introduzca la cantidad de objetos: "))
        precio= float(input("introduzca el precio unitario del objeto: "))
        total= precio * cantidad
        totalp = 0
        totalp = totalp + total
        id_objeto= input(str("Porfavor, introduzca el id del objeto que desea registrar: "))
        print("!Gracias, se guardaran los datos registrados!")
        print(f'El total es de {total}')
        objetos.write(f' ID = {id_objeto}')
        objetos.write(f' Objeto = {objeto}')
        objetos.write(f' Precio unitario = {precio}')
        objetos.write(f' Cantidad de objetos = {cantidad}')
        objetos.close
