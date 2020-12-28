class Coche():

    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if (self.__enmarcha):
            chequeo=self.__chequeo()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"

        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"

        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas.Un ancho de",self.__anchoChasis) 
    
    def __chequeo(self):
        print("Realizando chequeo interno")

        self.gasolina="oka"
        self.aceite="okay"
        self.puertas="cerradas"

        if (self.gasolina=="okay" and self.aceite=="okay" and self.puertas=="okay"):
            return True
        else:
            return False

miCarro=Coche()

print(miCarro.arrancar(True))
miCarro.estado()


print("------Seguimos creando objetos-----")


miCarro2=Coche()

print(miCarro2.arrancar(False))
miCarro2.estado()
