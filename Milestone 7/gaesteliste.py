#Funktionalität des Programms:
#es sollen gäste erfasst und gelöscht werden können 1/2
#es soll eine Liste ausgegeben werden, in der Vorname/nachname/gender ausgegeben wird /3
#es soll ein index der nutzer ausgegeben werden, der indexnummer und Vorname/nachname enthält /4
#es soll möglich sein einzelne Nutzer über deren index anzeigen zu lassen /5
#es soll möglich sein einzelne Nutzer auswählen und ändern zu können. /6
#das programm soll abgebrochen werden können /0x
#es soll eine dummyfunkrion zum speichernund eine zum laden berücksichtigt werden 8/9
#

#################################################################
# basisdefinitionen

# vornamen
# nachnamen
# telefonnummer
# email
# allergie
# gender

###############################################
#
gasteintrag = {}
gaestebuch = []
gi = {}
index = 0
gasteintrag1 = {}
###############################################
gasteintrag['vname'] = "Ben"
gasteintrag['nname'] = "Ertel"
gasteintrag['telnr'] = "+4900000000000"
gasteintrag['mail'] = "Ertel@ben.deutschland"
gasteintrag['allergie'] = "keine"
gasteintrag['gender'] = "backfisch"

#######################################################
# Beispiele
# gast in gaestebuch schreiben
#gaestebuch[0] = gasteintrag
gaestebuch.append(gasteintrag)

gasteintrag1['vname'] = "Horst"
gasteintrag1['nname'] = "Hammel"
gasteintrag1['telnr'] = "+4900000000000"
gasteintrag1['mail'] = "backt@packt.deutschland"
gasteintrag1['allergie'] = "(-.-)"
gasteintrag1['gender'] = "MWD"

#######################################################
# Beispiele
# gast in gaestebuch schreiben
#gaestebuch[0] = gasteintrag
gaestebuch.append(gasteintrag1)

# gasteintrag aus gaestebuch laden
#gasteintrag = gaestebuch[0]


##################################################################################
# hier kommt unser programm

def hauptmenue():
    print("Willkommen im Gäastebuch von Andreas!")
    print("\n\n")
    print("Für neu, Bitte 1 eingeben")
    print("Für anzeigen, Bitte 4 eingeben")
    print("Für ändern, Bitte 9 eingeben")

def neuereintrag():
    global gi               # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem Globalen Namespace in die Funktion laden
    global geastebuch       # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem Globalen Namespace in die Funktion laden

    gi.clear()
    print("Hier wird ein Neuer Gast eingetragen")
    gi['vname'] = input("Bitte den Vornamen eingeben:")
    gi['nname'] = input("Bitte den Nachname eingeben:")
    gi['telnr'] = input("Bitte den Telefonnummer eingeben:")
    gi['mail'] = input("Bitte den Mail eingeben:")
    gi['allergie'] = input("Bitte den Allergien eingeben:")
    gi['gender'] = input("Bitte den Geschlecht eingeben:")
    gaestebuch.append(gi)
    print("\n")

items = ['Vorname', 'Nachname', 'Tel. Nummer', 'Mail', 'Allergie', 'Gender']

def eintragaendern():
    global index
    gi = gaestebuch[index]
    anzahl = len(gaestebuch)

    print("Hier wird ein Neuer Gast eingetragen")
    gi['vname'] = input("Bitte den Vornamen eingeben:")
    gi['nname'] = input("Bitte den Nachname eingeben:")
    gi['telnr'] = input("Bitte den Telefonnummer eingeben:")
    gi['mail'] = input("Bitte den Mail eingeben:")
    gi['allergie'] = input("Bitte den Allergien eingeben:")
    gi['gender'] = input("Bitte den Geschlecht eingeben:")
    gaestebuch[index] = gi

    print("\n")

def eintragaendern1():

    global index

    gi = gaestebuch[index]

    print("Bitte Wähle aus, was geändert werden soll")
    print("1 " + items[0])
    print("2 " + items[1])
    print("3 " + items[2])
    print("4 " + items[3])
    print("5 " + items[4])
    print("6 " + items[5])


    altchoice = input("Bitte wähle aus, was gändert werden soll.")
    if altchoice == "1":
        print()


    if altchoice == "2":
        print()

    if altchoice == "3":
        print()

    if altchoice == "4":
        print()

# basisschleife aufbauen

def listuser():
    global gaestebuch
    counter = 0
    for gast in gaestebuch:
        #gast["vname"]
        #gast["nname"]
        print (counter.__str__() +" "+ gast["vname"] + " " + gast["nname"] )
        counter += 1



while True:
    # Hauptmenue ausgeben
    hauptmenue()
    # benutzereingabe abfragen
    hmeingabe = input("bitte wähle eine Option des Hauptmenüs:")

    #bedingung prüfen inclusive beingung "schleifenabbruch"
    #eintrag neuanlegen
    if hmeingabe == '1':
        print()
        neuereintrag()

    #liste der gäste anzeigen
    if hmeingabe == '4':
        print()
        listuser()

    #eintrag bearbeiten
    if hmeingabe == '9':
        print()
        eintragaendern()


    if hmeingabe == '0':
        print("Programm wird verlassen")
        break
    #gästebuch in eine string umwandeln und dann formatieren und  dann ausgeben.
    vaus = str(gaestebuch).replace('}, {', '},\n {')
    print(vaus)