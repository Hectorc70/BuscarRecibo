import re


class Buscador:
    """Busca los caracteres dados en un texto"""

    def __init__ (self, caracter_buscado, texto):

        self.palabra =  caracter_buscado
        self.texto = texto 

        self.buscar()
    
    
    def buscar(self):

        buscador = re.search(self.palabra, self.texto)

        if buscador:
            print("Se ha encontrado la palabra:", self.palabra)
        else:
            print("No se ha encontrado la palabra:", self.palabra)
