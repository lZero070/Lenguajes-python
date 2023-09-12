import random
from Operations import Operaciones

class Alfabeto(Operaciones):
    
    def __init__(self, simbolos):
        super().__init__(simbolos, tipo = Alfabeto)
                
    def get(self):
        return self.elementos
    
    def cerraduraEstrellas(self, nPalabras):
        palabras = set()
        palabras.add("#")   
        while(len(palabras) - 1 != nPalabras):
            cantR = random.randint(1, 20)
            palabraAleatoria = "".join(random.choices(self.elementos, k= cantR))
            if "#" not in palabraAleatoria:
                palabras.add(palabraAleatoria)
        return Alfabeto(palabras)
        
    def __str__(self):
        return f"{','.join(self.elementos)}"