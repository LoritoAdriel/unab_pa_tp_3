import Persona
        
class Libro:
    def __init__(self, titulo, autor, ISBN, páginas, edición, editorial, lugar, fecha_de_edición):
        self.titulo = titulo
        if not isinstance(autor, Persona):
            raise TypeError("El autor debe ser una instancia de Persona")
        self.autor = autor
        self.ISBN = ISBN
        if not isinstance(páginas,int):
            raise TypeError("El número de páginas debe ser un número entero")
        self.páginas = páginas
        self.edición = edición
        self.editorial = editorial
        self.lugar=lugar
        self.fecha_de_edición = fecha_de_edición
        
    #Getters
    @property
    def get_titulo(self):
        return self.titulo
    @property
    def get_autor(self):
        return self.autor
    @property
    def get_ISBN(self):
        return self.ISBN
    @property
    def get_páginas(self):
        return self.páginas
    @property
    def get_edición(self):
        return self.edición
    @property
    def get_editorial(self):
        return self.editorial
    @property
    def get_lugar(self):
        return self.lugar
    @property
    def get_fecha_de_edición(self):
        return self.fecha_de_edición
    
    #Setters
    @get_titulo.setter
    def set_titulo(self, titulo):
        self.titulo = titulo
    @get_autor.setter
    def set_autor(self, autor):
        self.autor = autor
    @get_ISBN.setter
    def set_ISBN(self, ISBN):
        self.ISBN = ISBN
    @get_páginas.setter
    def set_páginas(self, páginas):
        self.páginas = páginas
    @get_edición.setter
    def set_edición(self, edición):
        self.edición = edición
    @get_editorial.setter
    def set_editorial(self, editorial):
        self.editorial = editorial
    @get_lugar.setter
    def set_lugar(self, lugar):
        self.lugar = lugar
    @get_fecha_de_edición.setter
    def set_fecha_de_edición(self, fecha_de_edición):
        self.fecha_de_edición = fecha_de_edición
        
    def mostrar_informacion(self):
        return (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"ISBN: {self.isbn}\n"
                f"{self.editorial}, {self.lugar[0]} ({self.lugar[1]})\n"
                f"{self.fecha_edicion}\n"
                f"{self.paginas} páginas")
    
#Prueba
autor=Persona("Liang", "Y. Daniel")
libro = Libro(
    "Introduction to Java Programming 3a. edición", 
    autor, 
    "0-13-031997-X", 
    784, 
    "3a. edición", 
    "Prentice-Hall", 
    ("New Jersey", "USA"), 
    "viernes 16 de noviembre de 2001"
)
print(libro.mostrar_informacion())