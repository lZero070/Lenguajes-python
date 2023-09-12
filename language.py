import random
from Operations import Operaciones

class Lenguaje(Operaciones):
    
    def __init__(self, elementos):
        super().__init__(elementos, tipo = Lenguaje)
        
    def generarPalabras(self, alfabetos, cantidadPalabras):
        elementos = []
        for alfabeto in alfabetos:
            elementos += ["".join(random.choices([c for c in alfabeto.elementos if c != "#"], k=random.randint(1, 20))) for i in range(cantidadPalabras)]
        self.elementos = elementos
        
    def get(self):
        return self.elementos
    
    def concatenacion(self, otro):
        conca = []
        for palabra1 in self.elementos:
            for palabra2 in otro.elementos:
                conca.append(palabra1 + palabra2)      
        return Lenguaje(conca)
    
    def potencia(self, pot):
        poten = set("")
        if(pot == 0):
            return []
        elif(pot == 1):
            for palabra in self.elementos:
                poten.add(palabra)
        else:      
            for palabra1 in self.elementos:
                for palabra2 in self.potencia(pot-1):
                    poten.add(palabra2)
                    poten.add(palabra1 + palabra2)
        return poten
        
    def inversa(self):
        inver = []
        for palabra in self.elementos:
            aux = list(palabra)
            aux.reverse()
            inver.append("".join(aux))
        return Lenguaje(inver)
    
    def cardinalidad(self):
        return len(self.elementos)
    
    def __str__(self):
        return f"{', '.join(self.elementos)}"