from animal import Animal
class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
    
    #metodos get
    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas
    
    #metodos set
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    
    def setPatas(self, patas):
        self._patas = patas
    
    #metodos de la clase
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearCaballo(cls, nombre = "", edad = 0, genero = ""):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return caballo
    
    @classmethod
    def crearLeon(cls, nombre = "", edad = 0, genero = ""):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return leon