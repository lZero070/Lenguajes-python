import random
from Operations import Operations

class Alphabets(Operations):
    
    def __init__(self, symbols):
        super().__init__(symbols, category = Alphabets)
                
    def get(self):
        return self.elements
    
    def kleene_closure(self, n_words):
        words = set()
        words.add("#")   
        while(len(words) - 1 != n_words):
            quantity_R = random.randint(1, 20)
            random_word = "".join(random.choices(self.elements, k= quantity_R))
            if "#" not in random_word:
                words.add(random_word)
        return Alphabets(words)
        
    def __str__(self):
        return f"{','.join(self.elements)}"