class Stat:
    #setting the base of 10 and the modifier of 0
    def __init__(self, base=10, mod=0) :
        self.base = base
        self.mod = mod
    #applying any changes indicated in () to the base
    def apply_change (self,m=0) :
        self.base += m

    #returning the value of base to the function
    def get_value(self):
        return self.base
    #returning the value for mod after taking the base, subtracting 10 and dividing it in half
    def get_mod (self) :
        return int((self.base - 10)/2)

class Base_Stats :
    #creating dictionary with attributes asigned a base
    def __init__ (self) :
        #creating an empty dictionary called stats
        self.stats = {}
        for k in ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'] : 
            self.stats[k] = Stat()

