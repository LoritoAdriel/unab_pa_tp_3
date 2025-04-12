class Persona:
    def __init__(self, nombre, apellido):
        if not isinstance(nombre,str) or isinstance(apellido,str):
            raise TypeError("El nombre y el apellido deben ser una cadena de texto")
        self.nombre = nombre
        self.apellido = apellido
    
    #Getters
    @property
    def getNombre(self):
        return self.nombre
    @property
    def getApellido(self):
        return self.apellido
    
    #Setters
    @getNombre.setter
    def setNombre(self, nombre):
        if not isinstance(nombre,str):
            raise TypeError("El nombre debe ser una cadena de texto")
        self.nombre = nombre
    
    @getApellido.setter
    def setApellido(self, apellido):
        if not isinstance(apellido,str):
            raise TypeError("El apellido debe ser una cadena de texto")
        self.apellido = apellido
        
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    