#Copyright Benedikt Ertel 2022


eingabe = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
#eingabe = ' <html> ist eine tolle Sprache</html> '
#eingabe = "Hacker schleusen auch gerne Code ein! test()"
#eingabe = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
#eingabe = "Oder am Ende von Eingaben "
#eingabe = "Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch)\n"
#eingabe = "<dieser String ist nun sanitized>"
#eingabe = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
#eingabe = ' <html> ist eine tolle Sprache</html> '
#eingabe = "Hacker schleusen auch gerne Code ein! test()"
#eingabe = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
#eingabe = "Oder am Ende von Eingaben "
eingabe = """Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
#eingabe = """Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
#eingabe = "<dieser String ist nun sanitized>"


# daten ersetzen und austauschen
print("da wir jetzt wissen, wieviele Zeichen und welche Zeichenarten wir in unserer Eingabe haben, ersetzen wir diese dann")
print("\n\n\n")


# Sonderzeichen ersetzen
print("das war deine Eingabe " + eingabe)
print("\n\n\n")
print("ersetzen aller Sonderzeichen")


# definition von sonderzeichen die wir sanatizen
# sonderzeichen = "%$§\"\`\'#/:;-"
# klammern = "<>[]{}()"
# leerzeichen = " \t"
# zeilenumbruch = "\n\n\r"


# grundaufbau befehl:
# stringx = eingabe
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten
# print("es sind " + str(len(sonderz)) + " erfasst und zu bereinigen")
# charx = string.replace("zeichen", "ersatz")
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

############################################################
charx = sonderzeichen[1]
countx = stringx.count(sonderzeichen[1])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[2]
countx = stringx.count(sonderzeichen[2])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[3]
countx = stringx.count(sonderzeichen[3])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[4]
countx = stringx.count(sonderzeichen[4])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, "_")


############################################################
charx = sonderzeichen[5]
countx = stringx.count(sonderzeichen[5])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[6]
countx = stringx.count(sonderzeichen[6])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[7]
countx = stringx.count(sonderzeichen[7])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[8]
countx = stringx.count(sonderzeichen[8])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")

############################################################
charx = sonderzeichen[9]
countx = stringx.count(sonderzeichen[9])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[10]
countx = stringx.count(sonderzeichen[10])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[11]
countx = stringx.count(sonderzeichen[11])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[12]
countx = stringx.count(sonderzeichen[12])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[13]
countx = stringx.count(sonderzeichen[13])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


############################################################
charx = sonderzeichen[14]
countx = stringx.count(sonderzeichen[14])
out = "Sonderzeichen " + charx + " ist so oft vertretten: " + str(countx)
print(out)
sani1 = sani1.replace(charx, " ")


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

###########################################################

charx = klammern[1]
countk = sani1.count(klammern[1])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[1], " ")


###########################################################

charx = klammern[2]
countk = sani1.count(klammern[2])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[2], " ")


###########################################################

charx = klammern[3]
countk = sani1.count(klammern[3])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[3], " ")

###########################################################

charx = klammern[4]
countk = sani1.count(klammern[4])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[4], " ")

###########################################################

charx = klammern[5]
countk = sani1.count(klammern[5])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[5], " ")

###########################################################
charx = klammern[6]
countk = sani1.count(klammern[6])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[6], " ")


###########################################################
charx = klammern[7]
countk = sani1.count(klammern[7])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(klammern[7], " ")

###########################################################
print(sani1)
print("Nach der Bereinigung von Klammer! Weiter gehts mit den Leerzeichen!")
print("\n\n\n")
###########################################################
#jetzt kommen die Leerzeichen.

leerzeichen = " \t"

charx = leerzeichen[0]
countk = sani1.count(leerzeichen[0])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(leerzeichen[0], " ")

###########################################################

charx = leerzeichen[1]
countk = sani1.count(leerzeichen[1])
out = "Klammern " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(leerzeichen[1], " ")

###########################################################

print(sani1)
print("Nach der Bereinigung von Leerzeichen! Weiter gehts mit den Zeilenumbrüchen!")
print("\n\n\n")


###########################################################
zeile = "\n\n\r"
###########################################################
charx = zeile[0]
countk = sani1.count(zeile[0])
out = "Zeilenumbruch " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(leerzeichen[0], " ")


###########################################################
charx = zeile[1]
countk = sani1.count(zeile[1])
out = "Zeilenumbruch " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(zeile[1], " ")


###########################################################
charx = zeile[2]
countk = sani1.count(zeile[2])
out = "Zeilenumbrruch " + charx + " ist so oft vertretten: " + str(countk)
print(out)
sani1 = sani1.replace(zeile[2], " ")

###########################################################
print("So jetzt sind auch die Zeilenumbrüche weg und das ist dein Ergebnis  " + sani1)


