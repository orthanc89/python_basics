#Copyright Benedikt Ertel 2022

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

sonderzeichen = "%$§\"\`\'#/:;-.,~"

stringx = eingabe
############################################################
# Logischer Ablauf beachten!
charx = sonderzeichen[0]
countx = stringx.count(sonderzeichen[0])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = stringx.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[1]
countx = stringx.count(sonderzeichen[1])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[2]
countx = stringx.count(sonderzeichen[2])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[3]
countx = stringx.count(sonderzeichen[3])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[4]
countx = stringx.count(sonderzeichen[4])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, "_")
sleep(1)

############################################################
charx = sonderzeichen[5]
countx = stringx.count(sonderzeichen[5])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[6]
countx = stringx.count(sonderzeichen[6])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[7]
countx = stringx.count(sonderzeichen[7])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[8]
countx = stringx.count(sonderzeichen[8])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[9]
countx = stringx.count(sonderzeichen[9])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[10]
countx = stringx.count(sonderzeichen[10])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[11]
countx = stringx.count(sonderzeichen[11])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[12]
countx = stringx.count(sonderzeichen[12])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[13]
countx = stringx.count(sonderzeichen[13])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
charx = sonderzeichen[14]
countx = stringx.count(sonderzeichen[14])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")
sleep(1)

############################################################
print(sani1)
print("Nach der Bereinigung von Sonderzeichen! Weiter gehts mit den Klammern!")
print("\n\n\n")

###########################################################

klammern = "<>[]{}()"

charx = klammern[0]
countk = sani1.count(klammern[0])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani2k = sani1.replace(klammern[0], " ")
sleep(1)
###########################################################

charx = klammern[1]
countk = sani1.count(klammern[1])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[1], " ")
sleep(1)

###########################################################

charx = klammern[2]
countk = sani1.count(klammern[2])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[2], " ")
sleep(1)

###########################################################

charx = klammern[3]
countk = sani1.count(klammern[3])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[3], " ")
sleep(1)
###########################################################

charx = klammern[4]
countk = sani1.count(klammern[4])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[4], " ")
sleep(1)
###########################################################

charx = klammern[5]
countk = sani1.count(klammern[5])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[5], " ")
sleep(1)
###########################################################
charx = klammern[6]
countk = sani1.count(klammern[6])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[6], " ")
sleep(1)

###########################################################
charx = klammern[7]
countk = sani1.count(klammern[7])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[7], " ")
sleep(1)
###########################################################
print(sani1)
print("Nach der Bereinigung von Klammer! Weiter gehts mit den Leerzeichen!")
print("\n\n\n")
###########################################################
#jetzt kommen die Leerzeichen.

leerzeichen = " \t"

charx = leerzeichen[0]
countk = sani1.count(leerzeichen[0])
out = "Leerzeichen " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(leerzeichen[0], " ")
sleep(1)
###########################################################

charx = leerzeichen[1]
countk = sani1.count(leerzeichen[1])
out = "Leerzeichen " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(leerzeichen[1], " ")
sleep(1)
###########################################################

print(sani1)
print("Nach der Bereinigung von Leerzeichen! Weiter gehts mit den Zeilenumbrüchen!")
print("\n\n\n")
sleep(1)

###########################################################
zeile = "\n\n\r"
charx = zeile[0]
countk = sani1.count(zeile[0])
out = "Zeilenumbruch mit '\\n' " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(zeile[0], "")
sleep(1)

###########################################################
charx = zeile[1]
countk = sani1.count(zeile[1])
out = "Zeilenumbruch '\\n \\n' " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(zeile[1], "")
sleep(1)

###########################################################
charx = zeile[2]
countk = sani1.count(zeile[2])
out = "Zeilenumbruch mit '\\r' " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(zeile[2], "")
sleep(1)
###########################################################
print("So jetzt sind auch die Zeilenumbrüche weg und das ist dein 'sauberes' Ergebnis:  " + sani1)
sleep(2)

#charx = leerzeichen
#sani1 = sani1.count(leerzeichen[0])
#countx = sani1.replace(leerzeichen[0], )
#out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
#print(out)
#sleep(1)
