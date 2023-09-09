from collections import OrderedDict


class Operations:
    
    def __init__(self, elements, category):
        self.elements = elements
        self.category = category
    
    def __str__(self):
        return f"{','.join(self.elements)}"
    
    
    def union(self, other):
        elements = list(set(self.elements) | set(other.elements))
        return self.category(elements)
    
    def diferencia(self, other):
        elements = list(OrderedDict.fromkeys(set(self.elements) - set(other.elements)))
        return self.category(elements)
    
    def interseccion(self, other):
        elements = list(OrderedDict.fromkeys(set(self.elements) & set(other.elements)))
        return self.category(elements)