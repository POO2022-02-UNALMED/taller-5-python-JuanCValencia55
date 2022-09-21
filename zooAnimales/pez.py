from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "", cantidadAletas = ""):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)
    
    #metodos get
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    #metodos set
    def setColorEscamas(self, color):
        self._colorEscamas = color
    
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad
    
    #metodos de la clase
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    @classmethod
    def crearSalmon(cls, nombre = "", edad = 0, genero = ""):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones +=1
        return salmon

    @classmethod
    def crearBacalao(cls, nombre = "", edad = 0, genero = ""):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.salmones +=1
        return bacalao