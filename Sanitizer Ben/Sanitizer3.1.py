# Copyright Benedikt Ertel 2022

# module importieren da ich zu doof bin um counter() zum laufen zu bekommen https://de.acervolima.com/python-programm-zum-zahlen-von-grossbuchstaben-kleinbuchstaben-sonderzeichen-und-numerischen-werten-mit-regex/
import re

# systemfunktionen importieren
import sys

# zeitverzögerung importieren
from time import sleep

# sanatizer vs.2
# eingabe vom user
# intro
print('Erlebe die Zauberkraft von Python un der Bereinigung von Sonderzeichen und Befehlen')
print("\n\n\n")
eingabe = input("Bitte geben Sie hier ihre Eingabe ein. Sie darf Sonderzeichen, Zahlen und Buchstaben enthalten.")

print('Dann schauen wir mal')
print("\n")
print(eingabe)

check = len(eingabe)

if check < 1:
    print("Bitte geb etwas ein")
    print("Der rechner wird sich aufgrund der Falscheingabe selbstzerstören...")
    sleep(1)
    print("\n\n\n\n")
    print("4")
    sleep(1)
    print("\n\n\n\n")
    print("3")
    sleep(1)
    print("\n\n\n\n")
    print("2")
    sleep(1)
    print("\n\n\n\n")
    print("1")
    sleep(1)
    print("\n\n\n\n")
    print("0")
    sleep(1)
    print("\n\n\n\n")
    print("0")
    sleep(1)
    print("\n\n\n\n")
    sleep(1)
    print("hahahahahaha verarscht :P")
    print("\n\n\n\n")
    sys.exit()

# zahlen zählen
nummern = re.findall(r"[0-9]", eingabe)

# buchstaben zählen
grbuch = re.findall(r"[A-Z]", eingabe)
kleinbuch = re.findall(r"[a-z]", eingabe)

# sonderzeichen zählen
sonderz = re.findall(r"[%$§\"`*<>\[_|\]{}()#+'/:;-]", eingabe)

# Werte ausgebenprint
sleep(1)
print("Anzahl der Großbuchstaben: ", len(grbuch))
print("\n")
sleep(1)
print("Anzahl der Kleinbuchstaben: ", len(kleinbuch))
print("\n")
sleep(1)
print("Anzahl der Sonderzeichen: ", len(sonderz))
print("\n")
sleep(1)
print("Anzahl der numerischen Zeichen: ", len(nummern))
print("\n")

# daten ersetzen und austauschen

print("da wir jetzt wissen, wieviele Zeichen und welche Zeichenarten wir in unserer Eingabe haben, ersetzen wir diese dann")
print("\n\n\n")
sleep(2)

# Sonderzeichen ersetzen

print("das war deine Eingabe " + eingabe)
print("\n\n\n")
print("ersetzen aller Sonderzeichen")
sleep(1)

# bausteine bauen!
# definition von sonderzeichen die wir Sanatizen
# sonderzeichen = "%$§\"\`\'#/:;-"
# klammern = "<>[]{}()"
# leerzeichen = " \t"
# zeilenumbruch = "\n\n\r"
##############################################################
# charx = sonderzeichen[0]
# countx = stringx.count(sonderzeichen[0])
# out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
# print(out)
# sani1 = sani1.replace(charx, " ")
# sleep(1)


# Befehlsbaustein 2.0
startxs = "Sonderzeichen"
startxk = "Klammern"
startxl = "Leerzeichen"
startxz = "Zeilenumbrüche"
footerx = "ist so oft vertretten"
delmitter = ":"
########################################
#endausgabe vorbereiten
#befehlsstruktur:summe = 0
#countx = sani1.count(charx)
#summe = summe + countx
summe = 0
##########################################
#countxstr = str(stringx.count(charx)).zfill(2).rjust(5," ")
startxs = startxs.ljust(19," ")
startxk = startxk.ljust(19," ")
startxl = startxl.ljust(19, " ")
startxz = startxz.ljust(19, " ")
footerx = footerx.center(29, " ")
#out = startx + charx + footerx +  delmitter + countxstr

# grundaufbau befehl:
# string = input
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten
# print("es sind " + str(len(sonderz)) + " erfasst und zu bereinigen")
# charx = sting.replace("zeichen", "ersatz")
# charx = sonderzeichen[0]
# countx = string.count(sonderzeichen[0])
# out="Sonderzeichen " + charx + " ist  so oft vertreten :" + str(countx)
# print(out)
######################################
sonderzeichen = "%$&§\"\`\'#/:;-.,~"

############################################################
# Logischer Ablauf beachten!
sani1 = eingabe
charx = sonderzeichen[0]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)



############################################################
charx = sonderzeichen[1]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
############################################################
charx = sonderzeichen[2]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[3]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[4]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[5]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[6]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[7]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[8]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[9]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
############################################################
charx = sonderzeichen[10]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[11]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[12]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[13]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[14]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
############################################################
charx = sonderzeichen[15]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
print("\n")
print(sani1)
print("Nach der Bereinigung von Sonderzeichen! Weiter gehts mit den Klammern!")
print("\n\n\n")

###########################################################

klammern = "<>[]{}()"

charx = klammern[0]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################
charx = klammern[1]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

###########################################################

charx = klammern[2]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

###########################################################

charx = klammern[3]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################

charx = klammern[4]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################

charx = klammern[5]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################
charx = klammern[6]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

###########################################################
charx = klammern[7]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxk + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################
print("\n")
print(sani1)
print("Nach der Bereinigung von Klammer! Weiter gehts mit den Leerzeichen!")
print("\n\n\n")
###########################################################
# jetzt kommen die Leerzeichen.

leerzeichen = " \t"

charx = leerzeichen[0]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxl + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################

charx = leerzeichen[1]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxl + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################

print(sani1 + "\n")
print("Nach der Bereinigung von Leerzeichen! Weiter gehts mit den Zeilenumbrüchen!")
print("\n\n\n")
sleep(1)

###########################################################
zeile = "\n\n\r"
charx = zeile[0]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxz + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

###########################################################
charx = zeile[1]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxz + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

###########################################################
charx = zeile[2]
countx = sani1.count(charx)
summe = summe + countx
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxz + charx + footerx + delmitter + countxstr
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)
###########################################################
print("\n")
summe = str(summe)
print("So jetzt sind auch die Zeilenumbrüche weg und das ist dein 'sauberes' Ergebnis: \n\n " + sani1)
print("Dabei wurden " + summe.zfill(3).rjust(5, " ") + "Sonderzeichen ersetzt")
sleep(2)

# charx = leerzeichen
# sani1 = sani1.count(leerzeichen[0])
# countx = sani1.replace(leerzeichen[0], )
# out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
# print(out)
# sleep(1)
