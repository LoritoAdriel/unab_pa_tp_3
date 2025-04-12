class Cancion:
    def __init__(self, titulo, autor):
        if not isinstance(titulo, str) or not isinstance(autor,str):
            raise TypeError("El título y el autor deben ser cadenas de texto")
        self.titulo = titulo
        self.autor = autor
        
    #Getters
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    #Setters
    @autor.setter
    def autor(self, autor):
        if not isinstance(autor, str):
            raise TypeError("El autor debe ser una cadena de texto")
        self._autor = autor
        
    @titulo.setter
    def titulo(self, titulo):
        if not isinstance(titulo, str):
            raise TypeError("El título debe ser una cadena de texto")
        self._titulo = titulo