import random

class Wheel:

    def __init__(self):
        self.value = random.randrange(0, 37)

    def spinWheel(self): 
        self.value = random.randrange(0, 37)

    def winnerNumber(self): 
        return self.value
    
    def winnerColor(self): 

        def __BlackFirst():
            if self.value % 2 == 0: 
                return "BLACK"
            else: 
                return "RED"
            
        def __RedFirst():
            if self.value % 2 == 0: 
                return "RED"
            else: 
                return "BLACK"

        match self.value:
            case 0: 
                return "GREEN"
            
            case _ if 0 < self.value < 11: 
                return __BlackFirst()
                
            case _ if 10 < self.value < 19:
                return __RedFirst() 

            case _ if 18 < self.value < 29:
                return __BlackFirst()

            case _ if 28 < self.value:
                return __RedFirst()

        


