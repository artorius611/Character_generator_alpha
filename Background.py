import Race

class Acolyte () :
    def __init__ (self) :
        #creating the Acolyte Background and applying the bonus to stats
        self.stats = Race.Race_choice().stats
        print('Choose your Second Bonus:\nINT','    ','WIS')
        self.choice1 = input('')
        print('Choose your First Bonus:\nSTR','    ','INT','\nDEX','    ', 'WIS','\nCON','    ','CHA')
        self.choice2 = input('')
        self.stats[self.choice1].apply_change(2)
        if self.choice2 == self.choice1 :
            print ('You cant choose something you picked before')
        else:
            self.stats[self.choice2].apply_change(2)

class Background_selector () :
    #choosing the Background 
    def __init__ (self) :
        print('What is your background?\nAcolyte : 1')
        self.choice = int(input(''))
        if self.choice == 1 :
            self.stat = Acolyte()
