class vehiculo():

    def __init__(self,marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo: ", self.modelo, "\nEn marcha:",
            self.enmarcha,"\nAcelerando:",self.acelera, "\nFrenando:",self.frena)


class Furgoneta(vehiculo):
    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"



class Moto(vehiculo):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado(self):
        print("Marca:", self.marca, "\nModelo: ", self.modelo, "\nEn marcha:",
            self.enmarcha,"\nAcelerando:",self.acelera, "\nFrenando:",self.frena,
            "\n", self.hcaballito)

miMoto=Moto("Honda","CBY")

miMoto.caballito()

print(miMoto.estado())


miFurgoneta=Furgoneta("Renault","kanguro")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))