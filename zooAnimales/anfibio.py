from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre="", edad=0, habitat=" ", genero="", colorPiel = "", venenoso = False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    
    #metodos get
    def getColorPiel(self):
        return self._colorPiel
    
    def isVenenoso(self):
        return self._venenoso
    
    #metodos set
    def setColorPiel(self, color):
        self._colorPiel = color
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    
    #metodos de la clase 
    def movimiento(self):
        return "saltar"
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @classmethod
    def crearRana(cls, nombre = "", edad = 0, genero = ""):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return rana
    
    @classmethod
    def crearSalamandra(cls, nombre = "", edad = 0, genero = ""):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return salamandra