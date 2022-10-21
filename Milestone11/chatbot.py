# Copyright Benedikt Ertel
# -*- coding: utf-8 -*-
import random

###############################


##########################################
# grundvariablen
greeting = []
namen = []
endings = []
bekannte_eingabe = []
passende_antwort = []
random_antworten = []
###############################################
bekannte_eingabe.append("help")
passende_antwort.append('Dir kann man nicht helfen')
bekannte_eingabe.append('AGB')
passende_antwort.append('Liest du eh nicht! Die waschmaschine ist schon unterwegs!')
bekannte_eingabe.append('lotto')
passende_antwort.append('Seh ich wie eine glücksfee aus?')
bekannte_eingabe.append('witz')
passende_antwort.append('frag mal deine Mudda')
#################################################


random_antworten.append("Für Hilfe drücke F1 !!!")
random_antworten.append("Brudi!! Gib help ein !!")
random_antworten.append("Wenn ich dir nicht helfen kann, ALT+F4 drücken")
random_antworten.append("Ich sehe Geld in deinen Leben $$$$")
random_antworten.append("Sorry, ich wurde dafür nicht gut genug programmiert :D !!")
#################################################

greeting = ["Hallo User!", "Tagchen Nutzer!", "Ich hab dich erwartet User!", "Willkommen!"]
namen = ['Ingeborg', 'Bärbel', 'Irmgard', 'Friedhelm', 'Bob', 'Gustav', 'Martha', 'Leopold', 'Karla', 'Editha', 'Karl',
         'Ansgar', 'Franz']
endings = ['Tschüssikofsky', 'Paris, Athen, auf Wiedersehen', 'Ciao, Kakao', 'Auf Wiederhörnchen', 'Bis bald, im Wald',
           'Bis Baldrian', 'Bis spätersilie']
#########################################

#defs aufbauen

def freitext():
        global reaktion
        reaktion = {"hallo": "aber Hallo",
                              "geht": "Was verstehst du darunter?",
                              "essen": "Ich habe leider keinen Geschmackssinn :("
                              }
def neinname():
    global username

    if username == "nein" or username == "ja" or username == 0:
        print("Ich bin zwar nur ein Bot, aber ich möchte schon wissen, mit wem ich rede!")
        print('\n')
        username = ""
        username = input('Bitte nenn mir doch deinen namen: ')
        username = username.lower()
        if username == "nein" or username == "ja" or username == 0:
            print('Ja dann nicht' + random.choice(endings))
            running = False


def inhalt():
    global userx
    global item
    global random_antworten
    item = 0
    if running:
        print()
        items = bekannte_eingabe
        userx = ""
        print('Über folgendes kann ich mit dir reden, ' + username + ":" )
        print("\n")
        print(items[0])
        print(items[1])
        print(items[2])
        print(items[3])
        userx = input('Bitte wähle weise: ')
        userx = userx.lower()
        if userx == 'help':
            item += 1
        if userx == 'agb':
            item += 2
        if userx == 'lotto':
            item += 3
        if userx == 'witz':
            item +=4

        else:
            print(random.choice(random_antworten))
            running = False


def item0():
    global userx
    global username
    global item


    if user x == 'help':
        print()





# hauptmen
# ü
# hauptmenü starten und userername abfragen

running = True
global running
while running == True:
    global username
    print("\n\n")
    print()
    print(50 * "*")
    username = ""
    username = input("Hallo User, mein Name ist " + random.choice(namen) + " " + ", wie heißt du? ")
    username = username.lower()

    neinname()
    inhalt()
    item0()




if running == False:
    global running
    print(random.choice(endings) + username)





