class Animal:
    _totalAnimales = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = ""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
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
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\nAves : " + str(Ave.cantidadAves()) + "\nReptiles : " + str(Reptil.cantidadReptiles()) + "\nPeces : " + str(Pez.cantidadPeces()) + "\nAnfibios : " + str(Anfibio.cantidadAnfibios())
    
    def toString(self):
        if len(self._zona) == 0:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()
        return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es " + self._zona[0].getNombre() + ", en el " + self._zona[0].getZoo().getNombre()