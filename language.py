import random
from Operations import Operations

class Language(Operations):
    
    def __init__(self, elements):
        super().__init__(elements, category = Language)
        
    def generate(self, alphabets, quantitywords):
        elements = []
        for alphabet in alphabets:
            elements += ["".join(random.choices([c for c in alphabet.elements if c != "#"], k=random.randint(1, 20))) for i in range(quantitywords)]
        self.elements = elements
        
    def get(self):
        return self.elements
    
    def concatenation(self, other):
        concatenate = []
        for word1 in self.elements:
            for word2 in other.elements:
                concatenate.append(word1 + word2)      
        return Language(concatenate)
    
    def potency(self, pot):
        potency = set("")
        if(pot == 0):
            return []
        elif(pot == 1):
            for word in self.elements:
                potency.add(word)
        else:      
            for word1 in self.elements:
                for word2 in self.potency(pot-1):
                    potency.add(word2)
                    potency.add(word1 + word2)
        return potency
        
    def invert(self):
        revers = []
        for word in self.elements:
            aux = list(word)
            aux.reverse()
            revers.append("".join(aux))
        return Language(revers)
    
    def cardinality(self):
        return len(self.elements)
    
    def _str_(self):
        return f"{', '.join(self.elements)}"