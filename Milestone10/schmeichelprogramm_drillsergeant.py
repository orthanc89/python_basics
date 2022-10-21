#drillsergeant hartmann
import re
#moduile importieren
from time import sleep
import random
import sys

namex = ""

spruch1 = ['Endlich Frischfleisch zum Weichklopfen', 'Sie wollen in mein geliebtes Chor? Nehmen Sie erstmal 10 Kilo ab', 'Sie meinen auch, weil sie die letzten Jahre an dem Rock ihrer Mama genuckelt haben, sind Sie zu gut für mein geliebtes Chor!']

def aufnahme():
    global namex
    namex = input("Rekrut, wie heißen Sie? ")
    geschl = input("Rekrut " + namex + " Was sind Sie, (M)ännlein oder (W)eiblein?")
    geschl.lower()

    if geschl == 'm':
        print(random.choice(spruch1))

    elif geschl == 'w':
        print("Nur weil Sie Gott mit zwei Brüsten ausgestattet hat, werden Sie nicht weniger hart Arbeiten müssen, um in mein geliebtes Chor zu kommen")
        print(random.choice(spruch1))

    else:
        print("\n\n")
        print("Was sind Sie denn? Halten sie Sich für etwas besseres?")
        print("\n\n\n")
        sleep(1)
        print("Generation Schneeflocke, was? Wir brauchen hier keine Weicheier im Chor, raus! RAUS!")
        print("\n\n")
        sleep(1)
        print("Verlassen Sie mein geliebtes Chor!")
        sys.exit()

"""dies ist die funktion Meldung, die 2 Parameter übernimmt.
Meldung für den Meldungstext
pattern für das subpattern
    * vorbelegt mit wert: sir"""
def check_meldung(meldung,pattern='sir'):
    out = None
    meldung = meldung.lower()
    if meldung.startswith(pattern) and meldung.endswith(pattern):
        out = True
    else:
        out = False
    return out

def drill():
    fragen = []
    global namex
    sir1 = 0
    sir2 = 0
    sir3 = 0
    print("Ihr werdet mich nicht mögen weil ich hart bin!")
    sleep(1)
    print('\n\n')
    print("Ich werd euch schinden, bis ihr am verrecken seid! Ich schind euch, bis euch Buttermilch aus dem Arschloch läuft!")
    best = input("Haben Sie das Verstanden, Rekrut " + namex + "!")
    best = best.lower()
   # bestat = input("Rekrut! Das erste, was ich aus ihren Mund hören will, ist ein SIR und das letzte Wort ist auch ein Sir! Haben sie das verstanden?")
   # bestat = bestat.lower()

   # if len(sir1) < 1:
    if check_meldung(best,'sir'):
        print("Sehr gut Rekrut! Das Chor will Killermaschinen, keine Dummbatze!")


    else:
        blubb = input('Rekrut, Sie haben mich wohl nicht richtig Verstanden! Ich will am Anfang "Sir" und am Ende "Sir" Hören')

        if check_meldung(blubb, 'sir'):
            print("Rekrut " + namex + " Bei ihnen ist doch nicht alles verlohren")

#Hauptmenü bauen drillsergeant
while True:
    print('Willkommen im Chor Rekrut, ')

    alter = input('Rekrut bitte geben Sie ihr alter an in Zahlen!')
    if int(alter) >= 18 and int(alter) <= 65:

        print("Wählen Sie weise Rekrut, noch können Sie umkehren!")
        print("\n")
        userch = input("Start des Drills y, zum Beenden n ")
        userch.lower()


        if userch == 'y':
            print("Ihr Drillsergeant wird Sie gleich begrüßen!")
            sleep(2)
            print('Ich bin Gunnery Sergeant Hartman und zuständig für eure Grundausbildung!\n'
                  'Von nun an werdet ihr nur reden, wenn ihr angesprochen seid! \n'
                  'Und das erste und das letzte Wort aus eurem dreckigen Maul wird "Sir" sein! Habt ihr Maden das verstanden?')
            aufnahme()
            drill()
            print("\n\n")
            print("Willkommen auf den Reisfeldern, ihr Maden. Ihr wollt wohl die ersten sein, die einen Abschuss auf ihrer Karte haben, in meinem geliebten Chor")
            break

        elif userch == 'n':
            print("Sie sind eh zu schwach für mein geliebtes Chro, Feigling")
            sleep(3)
            break

        else:
            print("Ich werde Sie nochmals ganz einfach fragen! Wenn Sie das schon nicht hinbekommen, ist das Chor nichts für Sie")

    else:
        print('Sie sind nicht geeignet für unser Chor!')
        sys.exit()

