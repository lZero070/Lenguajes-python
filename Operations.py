from collections import OrderedDict


class Operaciones:
    
    def __init__(self, elementos, tipo):
        self.elementos = elementos
        self.tipo = tipo
    
    def __str__(self):
        return f"{','.join(self.elementos)}"
    
    
    def union(self, otro):
        elementos = list(set(self.elementos) | set(otro.elementos))
        return self.tipo(elementos)
    
    def diferencia(self, otro):
        elementos = list(OrderedDict.fromkeys(set(self.elementos) - set(otro.elementos)))
        return self.tipo(elementos)
    
    def interseccion(self, otro):
        elementos = list(OrderedDict.fromkeys(set(self.elementos) & set(otro.elementos)))
        return self.tipo(elementos)