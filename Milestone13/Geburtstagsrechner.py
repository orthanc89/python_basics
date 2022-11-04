#Erstelle eine Python-app in Milestone13 namens "Geburtstagsrechner.py"----

#Nutze das Time und das datetime Modul um einen kalender auf der python-shell anzeigen zu lassen.----------

#Dieser Kalender soll erst angezeigt werden, wenn ein menü eingeblendet wurde, in dem vom User eine Zeitzone (DE BEZ oder GMT)  ausgewählt wurde,------------
#und ein Geburtstag eingegeben wurde, der mittels date() entgegen genommen wurde.----------------------

#Hiernach sollen die TAge seit der Geburt sowie die Lebenszeit in Stunden (seit der Geburt) angezeigt wurde.-------------

#Am Ende soll eine weitere Abfrage kommen, in der die Gleiche Abfrage noch einmal kommt und bei geändertem Geburtsdatum,

#zusätzlich die Differenz zwischen den 2 Geburtsdaten angezeigt wird.

#Verwende hierzu eine Schleife, die mit der eingabe "Exit" abgebrochen werden kann.------------

#Erweitere das Programm so, das der Kalender wahlweise auf der Python-shell als Textcalender oder HTML-Kalender zur Anzeige gebracht wird.
#Die HTML-Version soll in folgende TAGs eingebettet werden.

#kopiere die Ausgabe der HTML-Ausgabe und kopiere diese in eine Textdatei mit der Endung HTML und Speichere diese ebenfalls in Milestone13 als "MyHtml-Kalender.htm".
#rufe diese Datei in einem Browser auf und schaue dir das Ergebnis an.
#lade den Milestone13 auf Teams und den B2-Server hoch.

import sys
import time
import datetime
import calendar
import locale

locale.setlocale(locale.LC_TIME, 'german')

#delta = datetime.timedelta(minutes=60)
#hours = delta.hours*24+delta.seconds/3600.0

def dateobj(gebuserday, gebusermonth, gebuseryear):

    gebdate = datetime.date(gebuseryear, gebusermonth, gebuserday)
    return gebdate

def timedeltaToHours(delta):
    daysToHours = delta.days * 24

    return daysToHours

def getdeltaobj(gebdateobj):
    today = datetime.date.today()
    delta = today - gebdateobj
    return delta

def menu():
    global deltahours
    print("\n")
    print("Willkommen zum Geburtstagsrechner von Holy-Bockwurst (c)")
    out = {'username':"",'exit':True, 'zeitzone':0, 'gebuserday':"", 'gebusermonth':"", 'gebuseryear':"", 'format':"cli"}
    # Name vom user erfragen & exit
    username = input("Bitte geb deinen Namen ein, zum Abbruch einfach EXIT eingeben: ")
    username = username.lower()
        #exitoption
    if username == "exit":
        sys.exit()

    else:
        out['username'] = username.capitalize()
        print('\n')

    zeitzone = input("In welcher Zeitzone befindest du dich (MEZ oder GMT)")

    if zeitzone == 'GMT':
        deltahours -= 1
        out['zeitzone'] = deltahours

    out['gebuserday'] = int(input("Bitte geben Sie ihr Geburtstagtag an:  "))
    print('\n')
    out['gebusermonth'] = int(input('Bitte geben Sie ihren Geburtsmonat an: (Als zahl: 1-12)'))
    print('\n')
    out['gebuseryear'] = int(input("Bitte geben Sie ihr Geburtsjahr an "))
    print('\n')
    ausgabe = 0
    ausgabe = int(input ("Wie möchtest du es?.... CLI[1] oder HTML[2] oder Python[3] oder GUI[4]"))

    if ausgabe >= 1 or ausgabe <= 4 :
        out['format'] = ausgabe
    else:
        out['format'] = 1
    return out

def outcli(ergebnis, deltadays, deltahours):
    print("Hallo, " + ergebnis['username'] + ", du bist: " + deltadays + " Tage alte, das sind: " + deltahours + " Stunden")
    kalenderblatt = calendar.TextCalendar(calendar.MONDAY)
    ausgabe = kalenderblatt.formatmonth(ergebnis["gebuseryear"], ergebnis["gebusermonth"])
    print(ausgabe)

def outhtml(ergebnis, deltadays, deltahours):
    x = False
    out = """<html>
<head></head>
<body>
<div>hier kommen die Berechnungen</div>
Hier kommt die Ausgabe
</body>
</html>"""

def outpython(ergebnis, deltadays, deltahours):
    x = False

def outgui(ergebnis, deltadays, deltahours):
    x=False

#hauptprogramm
running = True


while running == True:
    ergebnis = menu()
    running = ergebnis['exit']
    #inputersatz
    #gebuserday = "12"
    #gebusermonth = "2"
    #gebuseryear = "1989"

    gebuserday = int(ergebnis['gebuserday'])
    gebusermonth = int(ergebnis['gebusermonth'])
    gebuseryear = int(ergebnis['gebuseryear'])
    gebdateobj = dateobj(gebuserday,gebusermonth,gebuseryear)
    delta = getdeltaobj(gebdateobj)

    deltahours = str(timedeltaToHours(delta))
    deltadays = str(delta.days)

    if ergebnis["format"] == 1:
        outcli(ergebnis, deltadays, deltahours)

    elif ergebnis['format'] == 2:
        outhtml(ergebnis, deltadays, deltahours)

    elif ergebnis['format'] == 3:
        outpython(ergebnis, deltadays, deltahours)

    # alterstd = alter * 24
    # altermin = alterstd * 60
    #print(str(altertage.datetime.day) + "Tage seit Geburt vergangen, oder auch " + str(alterstundenfunc().datetime.hour)  + "Stunden, oder auch " + str(alterminfunc().minute) + "minuten.")

