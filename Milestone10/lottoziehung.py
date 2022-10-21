
#lottozahlenprogramm by nesli, saida und ben
#lottozahlen: 0-49
#superzahl 0-9
#aufsteigend
#keine doppelungen

#import modul random
import random
from time import sleep

#generelle definitonen
zahlenspeicher = []
#
zahlenspeicher.extend(range(1,50))

ziehung = random.sample(zahlenspeicher, 6)
#zahlen = range(1,50)
#zahlen = range(1,50)
ziehung.sort()
#ziehung.replace('[]'," ")

superzahl = range(1,11)

#lottozahl
#print(random.sample(zahlen, 6))
#zahlen = random.sample(zahlen, 6)
#zahlen = zahlen.sort()


#was für die augen

print("Willkommen beim Lotto-Automaten von Saida, Neslihan und Ben \n")
sleep(0.8)
print('um es kurz zu machen, ihr habt alle verloren und wir nehmen euch euer geld :P\n')
sleep(0.8)
print ('Nein spaß, natürlich geht die Ziehung gleich los\n')
sleep(0.8)
print('trommelwirbel!!!!!!!!!!!!\n\n')

print('Ihre 6 richtigen aus 49 lauten: ' + str(ziehung)[1:-1])

print("\n\n")
sleep(1.5)

#print('Die superzahl lautet: ' + join(random.sample(superzahl, 1)))

print('Die Superzahl lautet: ' + str(random.sample(superzahl, 1))[1:-1])
#superzahl

#durchlauf1
#durchlauf2 - durchlauf 1
#durchlauf3 - durchlauf2 - durchlauf 1
#durchhlauf4 -durchlauf3 - durchlauf2 - durchlauf 1
#durchlauf5 -durchhlauf4 -durchlauf3 - durchlauf2 - durchlauf 1
#durchlauf6 -durchlauf5 -durchhlauf4 -durchlauf3 - durchlauf2 - durchlauf 1


#superzahl =


#ausgabe