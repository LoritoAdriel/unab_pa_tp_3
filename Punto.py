import math

class Punto:
    def __init__(self, x, y):
        if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
            raise ValueError("Coordenadas deben ser números")
        self.x = x
        self.y = y
        
    #Getters
    @property
    def eje_x(self):
        return self.x
    
    @property
    def eje_y(self):
        return self.y
    
    #Setters
    @eje_x.setter
    def eje_x(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Coordenada debe ser un número")
        self.x = valor
    
    @eje_y.setter
    def eje_y(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Coordenada debe ser un número")
        self.y = valor
            
    def __str__(self):
        return f"({self.x}, {self.y})"
            
    def impresion(self):
        print(f"Punto {self}")
    
    @property   
    def opuesto(self):
        return Punto(-self.x, -self.y)
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distancia(self, otro):
        if not isinstance(otro, Punto):
            raise TypeError("Debe ser un objeto de la clase Punto.")
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Origen"

    def angulo(self):
        # Calcular el ángulo en radianes usando atan2
        angulo_radianes = math.atan2(self.y, self.x)
        
        # Convertir el ángulo a grados
        angulo_grados = math.degrees(angulo_radianes)
        
        return angulo_grados