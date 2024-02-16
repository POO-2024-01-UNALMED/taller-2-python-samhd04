class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if(color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        contador = 0

        for asiento in self.asientos:
            clase1 = str(type(asiento))
            clase1 = clase1.split(".")
            clase2 = clase1[1]
            clase2 = clase2.split("'")
            nombreClase = clase2[0]

            if nombreClase == "Asiento":
               contador = contador + 1
 
        return contador
        
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        elif self.registro == self.motor.registro:
            for asiento in self.asientos:
                clase1 = str(type(asiento))
                clase1 = clase1.split(".")
                clase2 = clase1[1]
                clase2 = clase2.split("'")
                nombreClase = clase2[0]

                if nombreClase == "Asiento":
                    if asiento.registro != self.registro or asiento.registro != self.motor.registro:
                        return "Las piezas no son originales"
        
        return "Auto original"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo



