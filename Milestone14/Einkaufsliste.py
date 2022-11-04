

import sys
#bitte die E-Book PDF- Seiten (pdf-seite) 198-221 bearbeiten
#ein neuen view erstelln und die Einkaufsliste erstellen,
#das Formular zur erstellung von personen vervollständigen
#eine Auswahl schreiben,  die auf der kommandline eine abfrage macht ob man die Person über die Shell oder die Gui anlegen möchte,
#und bei anlage über Gui, die root-pane erzeugt.
#beide ansichten sollen Ihre Daten als dict übergeben, die verarbeitung soll gui unabhängig gestaltet werden.
#schreibt dazu bitte ein paar funktionen und ladet eure ergebnisse in Git, in Teams und in den B2-Server unter Milestone14 hoch.
import tkinter as tk
######################
#dicts anlegen
ladenliste = ['Real','Marktkauf','Penny','Netto','Plus','Konti','Globus','Tengelmann', 'Jibi']
global zettelitem
zettelitem = {'pname':'', 'menge': '', 'preis':'', 'laden':''}
global personenitem
personenitem = {'vorname':'', 'nachname':'', 'alter':'', 'gender':''}
#items = ['Vorname', 'Nachname','Alter','Gender']
global einkaufsliste
einkaufsliste = []      #einkaufszettel enthält zettelitems
global personenliste
personenliste = []      #personenliste enthält personenitems
index = 0
#######################################################################
def climenu1():     #basisauswahl ob cli oder gui
    x = False


def cliekform():   #basis cli menü
    #global zettelitem
    global einkaufsliste
    zettelitem = {'pname': '', 'menge': '', 'preis': '', 'laden': ''}
    #zettelitem.clear()
    zettelitem['pname']= input('Bitte gib den Produktnamen ein')
    zettelitem['menge'] = input('Bitte gib die Menge ein')
    zettelitem['preis'] = input('Bitte gib den Preis ein')
    zettelitem['laden'] = input('Bitte gib den Laden ein')
    einkaufsliste.append(zettelitem)

def showclieinkaufsliste():
    global einkaufsliste
    for item in einkaufsliste:
        print('produkt: ' + item["pname"] + ' anz ' + item["menge"] + ' für ' + item["preis"] + ' bei ' + item["laden"])

def guiuserfsave():
    print('guiuserfsave')

def guiuserform(): #basis gui menu
    global root
    global frame
    for widgets in frame.winfo_children():
        widgets.destroy()

    label_vname = tk.Label(frame, text="Vorname", bg="silver").grid(row=1, column=1)
    eingabefeld_wert_vn = tk.StringVar()
    eingabefeld_vn=tk.Entry(frame, textvariable=eingabefeld_wert_vn).grid(row=1, column=2)

    label_nname = tk.Label(frame, text="Nachname", bg="silver").grid(row=2, column=1)
    eingabefeld_wert_nn = tk.StringVar()
    eingabefeld_nn = tk.Entry(frame, textvariable=eingabefeld_wert_nn).grid(row=2, column=2)

    label_alter = tk.Label(frame, text="Alter", bg="silver").grid(row=3, column=1)
    eingabefeld_wert_alt = tk.StringVar()
    eingabefeld_alt = tk.Entry(frame, textvariable=eingabefeld_wert_alt).grid(row=3, column=2)

    label_gen = tk.Label(frame, text="Gender", bg="silver").grid(row=4, column=1)
    eingabefeld_wert_gen = tk.StringVar()
    eingabefeld_gen = tk.Entry(frame, textvariable=eingabefeld_wert_gen).grid(row=4, column=2)

    schaltf1 = tk.Button(frame, text="Speichern", command=guiuserfsave)
    schaltf1.grid(row=5, column=1)

    schaltf2 = tk.Button(frame, text="Zurück", command=guihauptprogramm)
    schaltf2.grid(row=5, column=2)

global eingabefeld_wert_pn
global eingabefeld_wert_menge
global eingabefeld_wert_preis
global eingabefeld_wert_laden
def guiekfsave():
    print('gekfsave')

    global eingabefeld_wert_pn
    global eingabefeld_wert_menge
    global eingabefeld_wert_preis
    global eingabefeld_wert_laden
    #global zettelitem
    #zettelitem.clear()
    zettelitem = {'pname': '', 'menge': '', 'preis': '', 'laden': ''}

    zettelitem['pname']=eingabefeld_wert_pn.get()
    zettelitem['menge']=eingabefeld_wert_menge.get()
    zettelitem['preis']=eingabefeld_wert_preis.get()
    zettelitem['laden']=eingabefeld_wert_laden.get()
    einkaufsliste.append(zettelitem)

def guiekform():
    global root
    global eingabefeld_wert_pn
    global eingabefeld_wert_menge
    global eingabefeld_wert_preis
    global eingabefeld_wert_laden
    global frame

    for widgets in frame.winfo_children():
        widgets.destroy()

    label_pname = tk.Label(frame, text="Produktname", bg="silver").grid(row=1, column=1)
    eingabefeld_wert_pn = tk.StringVar()
    eingabefeld_pn = tk.Entry(frame, textvariable=eingabefeld_wert_pn).grid(row=1, column=2)

    label_menge = tk.Label(frame, text="Menge", bg="silver").grid(row=2, column=1)
    eingabefeld_wert_menge = tk.StringVar()
    eingabefeld_menge = tk.Entry(frame, textvariable=eingabefeld_wert_menge).grid(row=2, column=2)

    label_preis = tk.Label(frame, text="Preis", bg="silver").grid(row=3, column=1)
    eingabefeld_wert_preis = tk.StringVar()
    eingabefeld_preis = tk.Entry(frame, textvariable=eingabefeld_wert_preis).grid(row=3, column=2)

    label_laden = tk.Label(frame, text="Laden", bg="silver").grid(row=4, column=1)
    eingabefeld_wert_laden = tk.StringVar()
    eingabefeld_laden = tk.Entry(frame, textvariable=eingabefeld_wert_laden).grid(row=4, column=2)

    schaltf1 = tk.Button(frame, text="Speichern", command=guiekfsave)
    schaltf1.grid(row=5, column=1)

    schaltf2 = tk.Button(frame, text="Zurück", command=guihauptprogramm)
    schaltf2.grid(row=5, column=2)

def showguieinkaufsliste():
    global einkaufsliste
    global root
    global frame
    for widgets in frame.winfo_children():
        widgets.destroy()

    xrow = 0

    for item in einkaufsliste:
        x = False
        wwlabel = tk.Label(frame, text=item['pname'], bg="silver").grid(row=xrow, column=1)
        wwlabel = tk.Label(frame, text=item['menge'], bg="silver").grid(row=xrow, column=2)
        wwlabel = tk.Label(frame, text=item['preis'], bg="silver").grid(row=xrow, column=3)
        wwlabel = tk.Label(frame, text=item['laden'], bg="silver").grid(row=xrow, column=4)
        xrow += 1

    xrow += 1
    schaltf1 = tk.Button(frame, text="Zurück", command=guihauptprogramm)
    schaltf1.grid(row=xrow, column=1)


def clieinkaufsliste():    #einkaufsliste erstellen
    print('cliEKL Hallo')

    return zettelitem
def guieinkaufsliste():
    return zettelitem
####### cli def
def neuereintrag():
    #print('blubb')
    global personenitem  # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem Globalen Namespace in die Funktion laden
    global personenliste  # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem Globalen Namespace in die Funktion laden
    personenitem.clear()
    print("Hier wird ein Neuer Gast eingetragen")
    print('\n')
    personenitem['vname'] = input("Bitte den Vornamen eingeben:")
    personenitem['nname'] = input("Bitte den Nachname eingeben:")
    personenitem['gender'] = input("Bitte den Geschlecht eingeben [M/W/D]:")
    #personenliste.append(personenitem)
    print("\n")
    return personenitem

def listuser():
    global personenliste
    counter = 0
    for person in personenliste:
        # gast["vname"]
        # gast["nname"]
        print(counter.__str__() + " " + person["vname"] + " " + person["nname"])
        counter += 1
def eintragaendern():
    global index
    global personenliste
    global personenitem
    gi = personenliste[index]
    if len(personenliste) <= 0:
        print("Das gästebuch beinhaltet keine Gäste")
    else:
        gi = personenliste[index]
        listuser()
        print("\n")
        changevn = input("Bitte wählen Sie die Zahl  des Gastes aus, bei welchen was geändert werden soll")
        print("Bitte Wähle aus, was geändert werden soll")
        print("1 " + items[0])
        print("2 " + items[1])
        print("3 " + items[2])
        print("4 " + items[3])
        altchoice = input("Bitte wähle aus, was gändert werden soll.")
        if altchoice == "1":
            gi['vname'] = input("Bitte den neuen Vornamen eingeben:")
            print("Der neue Vorname lautet: " + gi['vname'])
            personenliste[index] = gi
        elif altchoice == "2":
            gi['nname'] = input("Bitte den neuen Nachnamen eingeben:")
            print("Der neue Nachname lautet: " + gi['nname'])
            personenliste[index] = gi
        elif altchoice == "3":
            gi['telnr'] = input("Bitte die neue Telefonnummer eingeben:")
            print("Die neue Nummer lautet: " + gi['telnr'])
            personenliste[index] = gi
        elif altchoice == "4":
            gi['gener'] = input("Bitte das neue Geschlecht eingeben")
            print("Der neue Nachname lautet: " + gi['nachname'])
            personenliste[index] = gi
def auswahlusercli():
    print('blubb')
    global personenliste
    auswahl = int(input('Bitte wähle aus: Personen Anlegen[1], Personen bearbeiten[2], Personen Anzeigen[3]: '))
    if auswahl == 1:
        personenliste.append(neuereintrag())
    elif auswahl == 2:
        eintragaendern()
    elif auswahl == 3:
        listuser()
    else:
        print('nö')


###############################################
def clihauptprogramm(): #hauptprogramm als cli
    while True:

        auswahlcli = int(input("Was möchtest du machen? Einkaufszettel[1]  oder Personen anzeigen[2]? Willst du die Einkaufsliste sehen[3] Abbruch[5]"))
        if auswahlcli == 1:
            cliekform()
        elif auswahlcli == 2:
            clihauptprogramm()
        elif auswahlcli == 3:
            showclieinkaufsliste()
        elif auswahlcli == 4:
            print("Hier ist noch nichts!!")
        elif auswahlcli == 5:
            sys.exit()

global root
global frame

def initgui():
    global root
    root = tk.Tk()
    global frame
    frame = tk.Frame(root)

def guihauptprogramm(): #hautprogramm als gui
    global root
    #root = tk.Tk()
    global frame

    #frame = tk.Frame(root)
    for widgets in frame.winfo_children():
        widgets.destroy()

    frame.grid(row=1, column=1)
    #frame.pack(side="top", expand=True, fill="both")
    schaltf1 = tk.Button(frame, text="Benutzer", command=guiuserform)
    schaltf1.grid(row=1 , column=1)
    schaltf2 = tk.Button(frame, text="Einkaufszettel", command=guiekform)
    schaltf2.grid(row=1 , column=2)
    schaltf3 = tk.Button(frame, text="Benutzer Liste", command=guiuserform)
    schaltf3.grid(row=2, column=1)
    schaltf4 = tk.Button(frame, text="Einkaufszettel Liste", command=showguieinkaufsliste)
    schaltf4.grid(row=2, column=2)

    #auswahl=int(input('Bitte wähle 0 für User oder 1 für Einkaufszettel'))
    #if auswahl == 0:

        #maske für benutzereingabe starten
        #guiuserform()
    #elif auswahl ==1:
        #oder maske für einkaufszettel starten
        #guiekform()

    root.mainloop()


def hauptprogramm():    #hauptprogramm basis
    auswahl = input ('Bitte wähle aus ob [CLI] oder [GUI]')
    print(auswahl)
    #auswahl = "gui"

    if auswahl == 'gui':
        initgui()
        guihauptprogramm()
    elif auswahl == 'cli':
        clihauptprogramm()
hauptprogramm()