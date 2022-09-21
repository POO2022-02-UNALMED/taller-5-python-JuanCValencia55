class Zoologico:
    def __init__(self, nombre = "", ubicacion = ""):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []


    #metodos get y set
    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion

    def getZona(self):
        return self._zonas

    #metodos de la clase
    def agregarZonas(self, zona):
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self):
        cantidad = 0

        for zona in self._zonas:
            cantidad += zona.cantidadAnimales()

        return cantidad