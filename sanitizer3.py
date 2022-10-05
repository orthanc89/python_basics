teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
teststring = ' <html> ist eine tolle Sprache</html> '
teststring = "Hacker schleusen auch gerne Code ein! test()"
teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
teststring = "Oder am Ende von Eingaben "
teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
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
print(columns2)
print(columns)

print("Hier kommt der Original-String nach Eingabe:\n")

print(teststring)
print(columns2)
print(columns)

print("dieser beinhaltet folgende Anzahl pro Sonderzeichen:")

#######################################
# Aufzählungen aufbereiten
print(columns2)
print(columns)
sani1 = teststring.casefold()

# Befehlsbaustein 2.0
startxs = "Sonderzeichen"
startxk = "Klammern"
startxl = "Leerzeichen"
startxz = "Zeilenumbrüche"
footerx = "ist so oft vertretten"
delmitter = ":"
countendx = 0

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


# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten
charx = sonderzeichen[0]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[1]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[2]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[3]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[4]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[5]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[6]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[7]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[8]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[9]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[10]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = sonderzeichen[11]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)
####################################################################################################
# anzahl Klammern ausgeben
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten

# print(columns2)
# print(columns)
charx = klammern[0]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = klammern[1]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = klammern[2]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = klammern[3]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = klammern[4]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = klammern[5]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = klammern[6]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

charx = klammern[7]
countx = sani1.count(charx)
countxstr = str(sani1.count(charx)).zfill(2).rjust(5, " ")
out = startxs + charx + footerx + delmitter + countxstr
countendx = countendx + countx
print(out)

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
print(columns2)
print(columns)
print("Stringinterne Bereinigung um Sonderzeichen.")
sani5 = sani1.replace(sonderzeichen[0], " ")
sani5 = sani5.replace(sonderzeichen[1], " ")
sani5 = sani5.replace(sonderzeichen[2], " ")
sani5 = sani5.replace(sonderzeichen[3], " ")
sani5 = sani5.replace(sonderzeichen[4], " ")
sani5 = sani5.replace(sonderzeichen[5], " ")
sani5 = sani5.replace(sonderzeichen[6], " ")
sani5 = sani5.replace(sonderzeichen[7], " ")
sani5 = sani5.replace(sonderzeichen[8], " ")
sani5 = sani5.replace(sonderzeichen[9], " ")
sani5 = sani5.replace(sonderzeichen[10], " ")
sani5 = sani5.replace(sonderzeichen[11], " ")
# sani5 = sani5.replace(sonderzeichen[12]," ")
# sani5 = sani5.replace(sonderzeichen[13]," ")
# sani5 = sani5.replace(sonderzeichen[14]," ")

print("Stringinterne Bereinigung von Klammern.")
sani5 = sani5.replace(klammern[0], " ")
sani5 = sani5.replace(klammern[1], " ")
sani5 = sani5.replace(klammern[2], " ")
sani5 = sani5.replace(klammern[3], " ")
sani5 = sani5.replace(klammern[4], " ")
sani5 = sani5.replace(klammern[5], " ")
sani5 = sani5.replace(klammern[6], " ")
sani5 = sani5.replace(klammern[7], " ")

print("Stringinterne Bereinigung von Zeilenumbrüchen.")
sani5 = sani5.replace(zeilenumbruch[0], " ")
sani5 = sani5.replace(zeilenumbruch[1], " ")
sani5 = sani5.replace(zeilenumbruch[2], " ")
# sani5 = sani5.replace(klammern[3]," ")
# sani5 = sani5.replace(klammern[4]," ")
# sani5 = sani5.replace(klammern[5]," ")
# sani5 = sani5.replace(klammern[6]," ")
# sani5 = sani5.replace(klammern[7]," ")
####################################################################################################
# Schlussendliche Ausgabe
# print(columns2)
# print(columns)
countendx = str(countendx).zfill(2).rjust(5, " ")
print("Es wurden " + countendx + " Sonderzeichen entfernt")
# noch einmal führende leerzeichen entfernen
# sani5 = sani5.lstrip(' ')
# print(sani5)
print('um Leerzeichen, Sonderzeichen und Klammern Bereinigter Text 5')
print('x->:' + sani5.capitalize())