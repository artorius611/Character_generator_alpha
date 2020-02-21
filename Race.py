from Stat import Base_Stats
import os
#importing the base statistics for attributes
myStat = Base_Stats()

class Dwarf : 
    def __init__ (self) :
        #setting the base stats for a dwarf by importing the base stats then using the function apply_change to modify them
        #included Ancestry free Stat
        self.stats = Base_Stats().stats
        self.stats.update({'HP' : 10})
        self.stats.update({'SPD' : 20})
        self.stats['CON'].apply_change(2)
        self.stats['WIS'].apply_change(2)
        self.stats['CHA'].apply_change(-2)
        self.choice = input('Coose your Bonus:\nSTR\nDEX\nINT\nCHA\n')
        self.stats[self.choice].apply_change(2)
        print ( "HP:", self.stats['HP'], '     ', 
                "Speed:", self.stats['SPD'],
                "\nSTR:", self.stats['STR'].get_value(),'', 'MOD:', self.stats['STR'].get_mod(), "      ", 'INT:', self.stats['INT'].get_value(),'', 'MOD:', self.stats['INT'].get_mod(),
                "\nDEX:", self.stats['DEX'].get_value(),'', 'MOD:', self.stats['DEX'].get_mod(), "      ", 'WIS:', self.stats['WIS'].get_value(),'', 'MOD:', self.stats['WIS'].get_mod(),
                "\nCON:", self.stats['CON'].get_value(),'', 'MOD:', self.stats['CON'].get_mod(), "      ", 'CHA:', self.stats['CHA'].get_value(),'', 'MOD:', self.stats['CHA'].get_mod(),)

class Elf : 
    def __init__ (self) :
        #setting the base stats for an Elf by importing the base stats then using the function apply_change to modify them
        #included Ancestry free Stat
        self.stats = Base_Stats().stats
        self.stats.update({'HP' : 6})
        self.stats.update({'SPD' : 30})
        self.stats['CON'].apply_change(-2)
        self.stats['DEX'].apply_change(2)
        self.stats['INT'].apply_change(2)
        self.choice = input('Coose your Bonus:\nSTR\nDEX\nINT\nCHA\n')
        self.stats[self.choice].apply_change(2)
        print ( "HP:", self.stats['HP'], '     ', 
                "Speed:", self.stats['SPD'],
                "\nSTR:", self.stats['STR'].get_value(),'', 'MOD:', self.stats['STR'].get_mod(), "      ", 'INT:', self.stats['INT'].get_value(),'', 'MOD:', self.stats['INT'].get_mod(),
                "\nDEX:", self.stats['DEX'].get_value(),'', 'MOD:', self.stats['DEX'].get_mod(), "      ", 'WIS:', self.stats['WIS'].get_value(),'', 'MOD:', self.stats['WIS'].get_mod(),
                "\nCON:", self.stats['CON'].get_value(),'', 'MOD:', self.stats['CON'].get_mod(), "      ", 'CHA:', self.stats['CHA'].get_value(),'', 'MOD:', self.stats['CHA'].get_mod(),)

class Human : 
    def __init__ (self) :
        #setting the base stats for an Elf and then giving the user the ability to choose there bonus
        #important note: currently if you choose the same value twice it does not apply the second one
        self.stats = Base_Stats().stats
        self.stats.update({'HP' : 8})
        self.stats.update({'SPD' : 25})
        print('Choose your First Bonus:\nSTR','    ','INT','\nDEX','    ', 'WIS','\nCON','    ','CHA')
        self.choice1 = input('')
        os.system ('cls')
        print('Choose your Second Bonus:\nSTR','    ','INT','\nDEX','    ', 'WIS','\nCON','    ','CHA')
        self.choice2 = input('')
        os.system ('cls')
        self.stats[self.choice1].apply_change(2)
        if self.choice2 == self.choice1 :
            print ('You cant choose something you picked before')
            print('Choose your Second Bonus:\nSTR','    ','INT','\nDEX','    ', 'WIS','\nCON','    ','CHA')
            self.choice2 = input('')
            os.system ('cls')
        else:
            self.stats[self.choice2].apply_change(2)
        print ( "HP:", self.stats['HP'], '     ', 
                "Speed:", self.stats['SPD'],
                "\nSTR:", self.stats['STR'].get_value(),'', 'MOD:', self.stats['STR'].get_mod(), "      ", 'INT:', self.stats['INT'].get_value(),'', 'MOD:', self.stats['INT'].get_mod(),
                "\nDEX:", self.stats['DEX'].get_value(),'', 'MOD:', self.stats['DEX'].get_mod(), "      ", 'WIS:', self.stats['WIS'].get_value(),'', 'MOD:', self.stats['WIS'].get_mod(),
                "\nCON:", self.stats['CON'].get_value(),'', 'MOD:', self.stats['CON'].get_mod(), "      ", 'CHA:', self.stats['CHA'].get_value(),'', 'MOD:', self.stats['CHA'].get_mod(),)

class Race_choice () :
    def __init__(self) :
        #creating a function to select the Race and then move to next section
        print ('What Race are you?\nHuman : 1\nDwarf : 2\nElf : 3')
        self.choice = int(input(''))
        #the command below clears the screen
        os.system ('cls')
        if self.choice == 1 :
            self.stats = Human()
        elif self.choice == 2 :
            self.stats = Dwarf()
        else:
            self.stats = Elf()
