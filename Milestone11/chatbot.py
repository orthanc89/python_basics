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
bekannte_eingabe.append('bye bye')
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
endings = ['Tschüssikofsky, ', 'Paris, Athen, auf Wiedersehen, ', 'Ciao, Kakao', 'Auf Wiederhörnchen, ', 'Bis bald, im Wald, ',
           'Bis Baldrian, ', 'Bis spätersilie, ']
#########################################

#defs aufbauen

#usernamen abfragen
def neinname():
    global username
    global running
    if username == "nein" or username == "ja" or username == 0 or username == '':
        print("Ich bin zwar nur ein Bot, aber ich möchte schon wissen, mit wem ich rede!")
        print('\n')
        username = ""
        username = input('Bitte nenn mir doch deinen namen: ')
        username = username.lower()
#username entspricht keinen namen
        if username == "nein" or username == "ja" or username == 0 or username == '':

            print('Ja dann nicht ' + ' ' + random.choice(endings))

            running = False #kill

###########################################################
#inhalt funktion
def inhalt():
    global userx
    global items
    global random_antworten
    global running
    global item
    global items
    item = 0

    if running:
        print()
        items = bekannte_eingabe #bekannte eingabe in items umwandeln
        userx = ""
        print('Über folgendes kann ich mit dir reden, ' + username + ":" )
        print("\n")
        print(items[0])
        print(items[1])
        print(items[2])
        print(items[3])
        print(items[4])
        userx = input('Bitte wähle weise: ')
        userx = userx.lower()
        #eingabe auf item erhöhen
        if userx == 'help':
            item += 1

        if userx == 'agb':
            item += 2

        if userx == 'lotto':
            item += 3

        if userx == 'witz':
            item +=4

        if userx == 'bye' or 'bye bye' or 'byebye':
            item +=5


        else: # falls die antwort nicht matched
            print(random.choice(random_antworten))

           # running = False

##############################################################
def item0():
    global userx
    global username
    global items
    global item
    global passende_antwort
    global endings

    if item >= 1:
        if item == 1:
            print(passende_antwort[0])

        if item == 2:
            print(passende_antwort[1])

        if item == 3:
            print(passende_antwort[2])

        if item == 4:
            print(passende_antwort[3])

        if item == 5: #kill
            print(random.choice(endings) + username)
            running = False
    else:
        print('Du musst schon was eingeben')


#####################################################

# hauptmenü
#
# hauptmenü starten und userername abfragen

running = True

while running == True:
    global username
    print("\n\n")
    print()
    print(50 * "*")
    username = ""
    username = input("Hallo User, mein Name ist " + random.choice(namen) + " " + ", wie heißt du? ")
    username = username.lower()
#usernamen abfragen und analysieren
    neinname()
#inhalt anzeigen
    inhalt()
#item ausgeben falls true
    item0()



#abbrruch variable
if running == False:
    print(random.choice(endings) + " " + username)





