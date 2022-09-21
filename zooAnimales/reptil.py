from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "", largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    
    #metodos get
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    #metodos set
    def setColorEscamas(self, color):
        self._colorEscamas = color
    
    def setLargoCol(self, largoCola):
        self._largoCola = largoCola
    
    #metodos de la clase
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @classmethod
    def crearIguana(cls, nombre = "", edad = 0, genero = ""):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas +=1
        return iguana
    
    @classmethod
    def crearSerpiente(cls, nombre = "", edad = 0, genero = ""):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes +=1
        return serpiente
