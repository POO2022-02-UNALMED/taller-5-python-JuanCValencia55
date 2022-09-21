from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from pez import Pez
from anfibio import Anfibio
class Animal:
    _totalAnimales = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = ""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        if len(self._zona) == 0:
            self._zona = []
        Animal._totalAnimales += 1
        
    #metodos get
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero
    
    def getZona(self):
        return self._zona[0]
    
    #metodos set
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setEdad(self, edad):
        self._edad = edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def setGenero(self, genero):
        self._genero = genero
    
    def setZona(self, zona):
        self._zona.append(zona)
    
    #metodos de la clase
    def movimiento(self):
        return "desplazarse"
    
    def totalPorTipo(self):
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\n" + "Aves: " + Ave.cantidadAves() + "\n" + "Reptiles: " + Reptil.cantidadReptiles() + "\n" + "Peces: " + Pez.cantidadPeces() + "\n" + "Anfibios: " + Anfibio.cantidadAnfibios()
    
    def toString(self):
        if len(self._zona) == 0:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + self.getEdad() + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()
        return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + self.getEdad() + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es " + self._zona[0].getNombre() + ", en el " + self._zona[0].getZoo().getNombre()