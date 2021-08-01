import random


class Borracho:
    """
    docstring
    """
    def __init__(self,name):
        self.name=name
    
class Borracho_tradicional(Borracho):
    """
    docstring
    """
    def __init__(self, name):
        super().__init__(name)
    
    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
