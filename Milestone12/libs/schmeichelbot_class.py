



#import
import random

#dic definieren
class schmeichelbot_class():
    def __init__(self):
        x= False

        self.adjektiv = []
        self.nomen = []

        self.adjektiv = ['schönste', 'beste', 'tollste', 'klügste']
        self.nomen = ['Mann', 'Programmierer', 'IT-Sibe']

    #erweiterung der nomen und adjektive
    def set_nomen(self,xnomen):
        self.nomen.append(xnomen)
        return self

    def set_adjektiv(self,xadjek):
        self.adjektiv.append(xadjek)
        return self

    def ausgabe(self):

        print('du bist der ' + random.choice(self.adjektiv) + ' ' + random.choice(self.nomen))

################################################################

#schmeichel = schmeichelbot_class()
#schmeichel.set_nomen("Hase").set_nomen("Bockwurst").set_nomen("Dummbatz")
#schmeichel.set_adjektiv('dümmste').set_adjektiv('flasche-leer-köpfigste').set_adjektiv('suboptimal-intelligent').set_adjektiv('intelligenzbenachteiligt')

#schmeichel.ausgabe()