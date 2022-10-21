
#import
import random
import sys

#zahlenbreich 1-10
#zähler der versuche
#eingabe vom user
#solange bis user richtig
#eine def(inition) mit while

#zahlen generieren und speichern
#zahlenspeicher = []
#zahlenspeicher.extend(range(1,11))


zufall = random.randint(1, 10)

counter = 0

def zufallszahl():
        global userin
        global zufall
        global counter

        while userin != zufall:

            if zufall == userin:
                print("Super, richtig geraten \n")
                print('Die Zufallszahl lautet: ' + str(zufall))
                break

            else:
                print("Bitte rate nochmal")
                userin = int(input("Bitte geb deine Zahl ein: \n"))
                print('Die Zufallszahl lautet: ' + str(zufall))
                counter += 1
                print("Du hast schon so oft falsch geraten: " + str(counter))

#eingang
print("Willkommen beim lustigen Zahlenraten von Saida, Nesli und Ben")
print("\n")
userin = int(input("Bitte geb eine Zahl ein: "))

if zufall == userin:
    print("Super du Ratefuchs")
    sys.exit()

elif zufall != userin:
    zufallszahl()

