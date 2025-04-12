class Linea:
    def __init__(self, _punto_a, _punto_b):
        if not isinstance(_punto_a,float) or not isinstance(_punto_b,float):
            raise ValueError("Coordenadas deben ser números flotantes")
        self.punto_a = _punto_a
        self.punto_b = _punto_b
        
    #Getters
    @property
    def get_punto_a(self):
        return self.punto_a
    
    @property
    def get_punto_b(self):
        return self.punto_b
    
    #Setters
    @get_punto_a.setter
    def set_punto_a(self, _punto_a):
        if not isinstance(_punto_a, float):
            raise ValueError("Coordenadas deben ser números flotantes")
        self.punto_a = _punto_a
        
    @get_punto_b.setter
    def set_punto_b(self, _punto_b):
        if not isinstance(_punto_b, float):
            raise ValueError("Coordenadas deben ser números flotantes")
        self.punto_b = _punto_b
        
    """Para poder mover los puntos en las distintas direcciones pense el punto_a como eje x
     y el punto_b como eje y"""
     
    def mueve_derecha(self,punto_eje_a):
        self.punto_a += punto_eje_a
        
    def mueve_izquierda(self,punto_eje_a):
        self.punto_a -= punto_eje_a
        
    def mueve_arriba(self,punto_eje_b):
        self.punto_b += punto_eje_b
    
    def mueve_abajo(self,punto_eje_b):
        self.punto_b -= punto_eje_b
        
    