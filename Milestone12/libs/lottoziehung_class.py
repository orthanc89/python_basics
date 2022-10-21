


#lottozahlenprogramm by nesli, saida und ben
#lottozahlen: 0-49
#superzahl 0-9
#aufsteigend
#keine doppelungen

#import modul random
import random
from time import sleep

class lottoziehung_class():

    def __init__(self):
        x = False

        #generelle definitonen
        self.zahlenspeicher = []

        self.zahlenspeicher.extend(range(1,50))
        self.superzahl = []
        self.superzahl.extend(range(1,11))

    def ziehung(self):
        ziehungx = random.sample(self.zahlenspeicher, 6)
        #zahlen = range(1,50)
        #zahlen = range(1,50)
        ziehungx.sort()
        #ziehung.replace('[]'," ")
        #ziehungx = self.ziehung
        return ziehungx

    def superzahl(self):
        self.superzahl = range(1,11)

    #lottozahl
    #print(random.sample(zahlen, 6))
    #zahlen = random.sample(zahlen, 6)
    #zahlen = zahlen.sort()

    def show_ziehung(self):
        x=False
        return str(self.ziehung())[1:-1]


    def show_superzahl(self):
        x=False
        return str(random.sample(self.superzahl, 1))[1:-1]



    #was für die augen
    def ausgabe(self):
        print("Willkommen beim Lotto-Automaten von Saida, Neslihan und Ben \n")
        #sleep(0.8)
        print('um es kurz zu machen, ihr habt alle verloren und wir nehmen euch euer geld :P\n')
        #sleep(0.8)
        print ('Nein spaß, natürlich geht die Ziehung gleich los\n')
        #sleep(0.8)
        print('trommelwirbel!!!!!!!!!!!!\n\n')

        print('Ihre 6 richtigen aus 49 lauten: ' + self.show_ziehung())

        print("\n\n")
        #sleep(1.5)

        #print('Die superzahl lautet: ' + join(random.sample(superzahl, 1)))

        print('Die Superzahl lautet: ' + self.show_superzahl())
        #superzahl

#lottospiel
#lotto = lottoziehung_class()
#lotto.ziehung()
#lotto.ausgabe()




    #durchlauf1
    #durchlauf2 - durchlauf 1
    #durchlauf3 - durchlauf2 - durchlauf 1
    #durchhlauf4 -durchlauf3 - durchlauf2 - durchlauf 1
    #durchlauf5 -durchhlauf4 -durchlauf3 - durchlauf2 - durchlauf 1
    #durchlauf6 -durchlauf5 -durchhlauf4 -durchlauf3 - durchlauf2 - durchlauf 1


    #superzahl =


    #ausgabe