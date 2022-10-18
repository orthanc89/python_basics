import csv
from time import sleep


#Funktionalität des Programms:
#es sollen gäste erfasst und gelöscht werden können 1/2 check
#es soll eine Liste ausgegeben werden, in der Vorname/nachname/gender ausgegeben wird /4/1
#es soll ein index der nutzer ausgegeben werden, der indexnummer und Vorname/nachname enthält /4 check
#es soll möglich sein einzelne Nutzer über deren index anzeigen zu lassen /5
#es soll möglich sein einzelne Nutzer auswählen und ändern zu können. /6
#es soll eine dummyfunkrion zum speichern und eine zum laden berücksichtigt werden 8/9
##das programm soll abgebrochen werden können /0x

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
gaestebuch = []
gasteintrag = {}
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
gaestebuch.append(gasteintrag)
#######################################################
# Beispiele
# gast in gaestebuch schreiben
#gaestebuch[0] = gasteintrag
gasteintrag1 = {}

gasteintrag1['vname'] = "Horst"
gasteintrag1['nname'] = "Hammel"
gasteintrag1['telnr'] = "+4900000000000"
gasteintrag1['mail'] = "backt@packt.deutschland"
gasteintrag1['allergie'] = "(-.-)"
gasteintrag1['gender'] = "MWD"
gaestebuch.append(gasteintrag1)
############################################################
gasteintrag2 = {}

gasteintrag2['vname'] = "Peter"
gasteintrag2['nname'] = "pan"
gasteintrag2['telnr'] = "+4900000000000"
gasteintrag2['mail'] = "pan@pfanne.deutschland"
gasteintrag2['allergie'] = "Q(-.-Q)"
gasteintrag2['gender'] = "doof"
gaestebuch.append(gasteintrag2)
#######################################################
# Beispiele
# gast in gaestebuch schreiben
#gaestebuch[0] = gasteintrag


# gasteintrag aus gaestebuch laden
#gasteintrag = gaestebuch[0]


##################################################################################
# hier kommt unser programm

def hauptmenue():

    print("\n\n\n")
    print("Willkommen im Gästebuch von Andreas!")
    print("\n\n")
    print("Für neu, Bitte 1 eingeben")
    print("Für anzeigen, Bitte 4 eingeben")
    print("Für das anzeigen von Gast plus zusatzinfos, Bitte 5 Eingeben")
    print("Für exportieren, Bitte die 7 eingeben")
    print("Für ändern, Bitte 8 eingeben")
    print("Für löschen, Bitte 9 eingeben")
    print("Für beenden, Bitte 0 eingeben")

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
    global gaestebuch
    global gasteintrag
    gi = gaestebuch[index]

    if len(gaestebuch) <= 0:
        print("Das gästebuch beinhaltet keine Gäste")

    else:
        gi = gaestebuch[index]
        listuser()
        print("\n")
        changevn = input("Bitte wählen Sie die Zahl  des Gastes aus, bei welchen was geändert werden soll")


        print("Bitte Wähle aus, was geändert werden soll")
        print("1 " + items[0])
        print("2 " + items[1])
        print("3 " + items[2])
        print("4 " + items[3])
        print("5 " + items[4])
        print("6 " + items[5])
        print("\n")

        altchoice = input("Bitte wähle aus, was gändert werden soll.")

        if altchoice == "1":
            gi['vname'] = input("Bitte den neuen Vornamen eingeben:")
            print ("Der neue Vorname lautet: " + gi['vname'])
            gaestebuch[index] = gi

        if altchoice == "2":
            gi['nname'] = input("Bitte den neuen Nachnamen eingeben:")
            print("Der neue Nachname lautet: " + gi['nname'])
            gaestebuch[index] = gi

        if altchoice == "3":
            gi['telnr'] = input("Bitte die neue Telefonnummer eingeben:")
            print("Die neue Nummer lautet: " + gi['telnr'])
            gaestebuch[index] = gi

        if altchoice == "4":
            gi['mail'] = input("Bitte die neue Mail eingeben:")
            print("Die neue Mail lautet: " + gi['mail'])
            gaestebuch[index] = gi

        if altchoice == "5":
            gi['allergie'] = input("Bitte die neue Allergie eingeben:")
            print("Die neue Allergie: " + gi['allergie'])
            gaestebuch[index] = gi

        if altchoice == "6":
            gi['gener'] = input("Bitte das neue Geschlecht eingeben")
            print("Der neue Nachname lautet: " + gi['nachname'])
            gaestebuch[index] = gi


# basisschleife aufbauen

#user aufzeigen
def listuser():
    global gaestebuch
    counter = 0
    for gast in gaestebuch:
        #gast["vname"]
        #gast["nname"]
        print (counter.__str__() +" "+ gast["vname"] + " " + gast["nname"] )
        counter += 1

def listuserpara():
    global index
    global gaestebuch
    global gasteintrag
    gi = gaestebuch[index]
    counter = 0
    variax = 0
    print ("Folgende Gäste sind eingetragen")
    listuser()
    print("\n\n")
    print(40*'-')
    for gast in range(len(gaestebuch)):
        print("3 " + items[2])
        print("4 " + items[3])
        print("5 " + items[4])
        print("6 " + items[5])
        print("\n")
        variax = input("Bitte Wähle aus, was angezeigt werden soll werden soll zum Vornamen und Nachnamen: ")
        variax = int(variax)

        print (counter.__str__() + " " + gast["vname"] + " " + gast["nname"] + " " + items[variax])
        counter += 1


#eintrag ändern
def eintragdel():

    global gaestebuch
    listuser()
    zahl = input("Welcher Gast soll gelöscht werden (Nummer)")
    zahl = int(zahl)
    del(gaestebuch[zahl])

#exportieren
def export():
    global gaestebuch
    global gi

    try:

        with open('gaestebuch.csv', 'w') as f:
            items = ['Vorname', 'Nachname', 'Tel. Nummer', 'Mail', 'Allergie', 'Gender']
            writer = csv.DictWriter(f, fieldnames = items)
            writer.writeheader()
            for items, gi in dict.gaestebuch():
                w.writeriw([items, gi])
            #for elem in gi:
                #writer.writerow(elem)
                print("Export erfolgreich!")
                sleep(1)
    except IOError:
        print ("Fehler in der ein und oder ausgabe, Bitte wenden Sie an ihren lokalen SUDO-Admin")

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

    #liste der User mit bestimmten parametern anzeigen lassen
    if hmeingabe == "5":
        listuserpara()

    #export
    if hmeingabe == '7':
        export()

    #eintrag bearbeiten
    if hmeingabe == '8':
        print()
        eintragaendern1()

    #eintrag löschen
    if hmeingabe == '9':
        print()
        eintragdel()

    #programm beenden
    if hmeingabe == '0':
        print("Programm wird verlassen")
        break
    #gästebuch in eine string umwandeln und dann formatieren und  dann ausgeben.
    vaus = str(gaestebuch).replace('}, {', '},\n {')
    #print(vaus)