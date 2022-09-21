from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal

if __name__ == "__main__":
    zoo = Zoologico("Zoologico Central", "Chicago")
    z1 = Zona("zona1")
    z2 = Zona("zona2")
    zoo.agregarZonas(z1)
    zoo.agregarZonas(z2)
    z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
    z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
    z1.agregarAnimales(Mamifero.crearLeon("test", 11, "M"))
    z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
    z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
    z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
    z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
    z1.agregarAnimales(Anfibio.crearRana("test", 11, "M"))
    z2.agregarAnimales(Anfibio.crearSalamandra("test", 11, "M"))
    z2.agregarAnimales(Reptil.crearIguana("test", 11, "M"))
    z2.agregarAnimales(Reptil.crearSerpiente("test", 11, "M"))
    z2.agregarAnimales(Pez.crearSalmon("test", 11, "M"))
    z2.agregarAnimales(Pez.crearBacalao("test", 11, "M"))
    Mamifero.crearCaballo("test", 11, "M")
    Ave.crearHalcon("test", 11, "M")
    Anfibio.crearRana("test", 11, "M")
    Reptil.crearIguana("test", 11, "M")
    Pez.crearBacalao("test", 11, "M")

    print(Pez.bacalaos)
    print(Pez.salmones)