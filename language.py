import random
from Operations import Operations

class Language(Operations):
    
    def _init_(self, elements):
        super().__init__(elements, category = Language)
        
    def generateWords(self, alphabets, numberOfWords):
        elements = []
        for alphabet in alphabets:
            elements += ["".join(random.choices([c for c in alphabet.elementos if c != "#"], k=random.randint(1, 20))) for i in range(numberOfWords)]
        self.elements = elements
        
    def get(self):
        return self.elements
    
    def concatenation(self, other):
        result = []
        for word1 in self.elements:
            for word2 in other.elements:
                result.append(word1 + word2)      
        return Language(result,category=Language)
    
    def power(self, exponent):
        powerset = set("")
        if(exponent == 0):
            return []
        elif(exponent == 1):
            for word in self.elements:
                powerset.add(word)
        else:      
            for word1 in self.elements:
                for word2 in self.power(exponent-1):
                    powerset.add(word2)
                    powerset.add(word1 + word2)
        return powerset
        
    def inverse(self):
        inverselist = []
        for word in self.elements:
            aux = list(word)
            aux.reverse()
            inverselist.append("".join(aux))
        return Language(inverselist,category = Language)
    
    def cardinality(self):
        return len(self.elements)
    
    def _str_(self):
        return f"{', '.join(self.elements)}"