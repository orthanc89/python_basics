teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
#teststring = ' <html> ist eine tolle Sprache</html> '
#teststring = "Hacker schleusen auch gerne Code ein! test()"
#teststring = "hacker schleusen auch gerne Code ein! test()"
#teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
#teststring = "Oder am Ende von Eingaben "
#teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
#teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
# teststring = "<dieser String ist nun sanitized>"
# teststring = ' dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - '
# teststring = " dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - "
# teststring = " dies ist ein Teststring(); \nmit Klammern und <html tags>! \n und Umbrüchen - "
# teststring = " dies ist ein Teststring(); \rmit Klammern und <html tags>! \r und Umbrüchen - "


#############################################################################
# Basisdefinition von Werten und Strings
columns = "123456789012345678901234567890123456789012345678901234567890"
columns2 = "000000000111111111122222222223333333333444444444455555555556"
sonderzeichen = "%$§\"\`\'#/:;-"
leerzeichen = " \t"
zeilenumbruch = "\n\n\r"
klammern = "<>[]{}()"

############################################################################
# Ausgabe vorbereiten
#print(columns2)
#print(columns)

print("Hier kommt der Original-String nach Eingabe:\n")

print(teststring)
#print(columns2)
#print(columns)

print("dieser beinhaltet folgende Anzahl pro Sonderzeichen:")

#######################################
# Aufzählungen aufbereiten
#print(columns2)
#print(columns)
sani1 = teststring.casefold()

# Basisvariablen 2.0
startxs = "sonderzeichen"
startxk = "klammern"
startxl = "leerzeichen"
startxz = "zeilenumbrüche"
footerx = "ist so oft vertretten"
delmitter = ":"
countendx = 0
endlist = []
ausgabeliste = []

# countxstr = str(stringx.count(charx)).zfill(2).rjust(5," ")
startxs = startxs.ljust(19, " ")
startxk = startxk.ljust(19, " ")
startxl = startxl.ljust(19, " ")
startxz = startxz.ljust(19, " ")
footerx = footerx.center(29, " ")
# out = startx + charx + footerx +  delmitter + countxstr

# Logischer Ablauf beachten!
# grundbaustein
# sani1 = eingabe
# charx = sonderzeichen[0]

# countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
# out = startxs + charx + footerx + delmitter + countxstr
# countent = countend + countx
# print(out)
# sani1 = sani1.replace(charx, " ")
######################################################
startx = 1
abbruchx = len(sonderzeichen)


#while schleife grundbaustein
# while startx <= abbruchx:
# vsz = startx - 1
# charx = sonderzeichen[vsz]
# countx = sani1.count(charx)
# countxstr = str(sani1.count(charx)).zfill(4).rjust(5, " ")
# out = startxs + charx + footerx + delmitter + countxstr
# countendx = countendx + countx
# print(out)

#while schleife grundbaustein
# startcounter (startx) muss erhöht werden !
while startx <= abbruchx:
     vsz = startx - 1
     charx = sonderzeichen[vsz]
     countx = sani1.count(charx)
     countxstr = str(sani1.count(charx)).zfill(4).rjust(5, " ")
     out = startxs.capitalize() + charx + footerx + delmitter + countxstr
     ausgabeliste.append(out)
     countendx = countendx + countx
     startx += 1

# coundendx in endlist eintragen
endlist.append(countendx)

#print(countendx)

###############################################################
abbruchxk = len(klammern)
durchlauf = 1
countendkl = 0
while durchlauf <= abbruchxk:
     vsz = durchlauf - 1
     charx = klammern[vsz]
     countx = sani1.count(charx)
     countxstr = str(sani1.count(charx)).zfill(4).rjust(5, " ")
     out = startxk.capitalize() + charx + footerx + delmitter + countxstr
     countendkl = countendkl + countx
     ausgabeliste.append(out)
     durchlauf += 1
#countendkl in endlist eintragen
endlist.append(countendkl)

#print(countendkl)

###################################################################################################
# Grundsätzliche Bearbeitung zu Eingabefehlern und Bösen Eingabe Anfängen und Enden!
# print(columns2)
# print(columns)


print("Basisbearbeitung des Strings ")
# Leerzeichen am Anfang und Ende, sicher entfernen
sani1 = teststring.strip(leerzeichen)
sani1 = sani1.replace(zeilenumbruch[0], " ")
sani1 = sani1.replace(zeilenumbruch[1], " ")
sani1 = sani1.replace(leerzeichen[1], " ")

print('Um Leerzeichen Bereinigter String 1:\n' + sani1)
############################################################################
# Klammern am Anfang und Ende entfernen !
sani2 = sani1.strip(klammern)
print('Um Klammern Bereinigter Text 2:\n' + sani2)

# Klammern und Leerzeichen am Anfang und Ende entfernen
sani3 = sani2.strip(klammern)
print('Um Klammern und Leerzeichen Bereinigter Text 3:\n' + sani3)

# Sonderzeichen für Programmierung am Ende entfernen!
# String 3 weiterverarbeiten
sani1 = sani3.strip(sonderzeichen)
print('Um SonderzeichenBereinigter Text 4\n' + sani1)

###################################################################################################
# Durchführung der Bereinigung
#print(columns2)
#print(columns)


print("Stringinterne Bereinigung um Sonderzeichen.")

durchlauf = 1
abbruch = len(sonderzeichen)
############################################
#grundbaustein:
#while durchlauf <= abbruch:
#   dnummer = durchlauf - 1
#   sani5 = sani1.replace(sonderzeichen[dnummer], " ")
#   durchlauf += 1
########################################################
#Ersetzen der Sonderzeichen
sani5 = sani1
while durchlauf <= abbruch:
    dnummer = durchlauf - 1
    sani5 = sani5.replace(sonderzeichen[dnummer], " ")
    durchlauf += 1
########################################################
# klammern ersetzen
print("Stringinterne Bereinigung von Klammern.")
durchlauf = 1
abbruch =  len(klammern)
#######################################################
while durchlauf <= abbruch:
    dnummer = durchlauf - 1
    sani5 = sani5.replace(klammern[dnummer], " ")
    durchlauf += 1
 ######################################################
# Zeilenumbürrche ersetzen
print("Stringinterne Bereinigung von Zeilenumbrüchen.")
durchlauf = 1
abbruch =  len(zeilenumbruch)
#######################################################
while durchlauf <= abbruch:
    dnummer = durchlauf - 1
    sani5 = sani5.replace(zeilenumbruch[dnummer], " ")
    durchlauf += 1

####################################################################################################
# Schlussendliche Ausgabe
# print(columns2)
# print(columns)
countendx = countendx + countendkl
countendx = str(countendx).zfill(2).rjust(5, " ")
print("Es wurden " + countendx + " Sonderzeichen entfernt")
# noch einmal führende leerzeichen entfernen
# sani5 = sani5.lstrip(' ')
# print(sani5)

durchlauf = 1
abbruch = len(ausgabeliste)
while durchlauf <= abbruch:
    anr = durchlauf -1
    print(ausgabeliste[anr])
    durchlauf += 1

print(abbruch)
sani5 = sani5.strip(" ")
print(endlist)
print('der um Leerzeichen, Sonderzeichen und Klammern Bereinigter Text: ')
print('Eingabe bereinigt->:' + sani5.capitalize())