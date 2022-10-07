#teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
#teststring = ' <html> ist eine tolle Sprache</html> '
#teststring = "Hacker schleusen auch gerne Code ein! test()"
#teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
#teststring = "Oder am Ende von Eingaben "
#teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
#teststring = "<dieser String ist nun sanitized>"
#teststring = ' dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - '
#teststring = " dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - "
#teststring = " dies ist ein Teststring(); \nmit Klammern und <html tags>! \n und Umbrüchen - "
#teststring = " dies ist ein Teststring(); \rmit Klammern und <html tags>! \r und Umbrüchen - "
#teststring = "% dies ist ein Teststring(); \rmit Klammern und <html tags>! \r und Umbrüchen - "
#teststring = "§$%&$%§$%$&&%/&()*'*'*''"

#############################################################################
# Basisdefinition von Werten und Strings
columns = "123456789012345678901234567890123456789012345678901234567890"
columns2 = "000000000111111111122222222223333333333444444444455555555556"
sonderzeichen = "%$§\"\`\'#/:;-="
leerzeichen = " \t"
zeilenumbruch = "\n\n\r"
klammern = "<>[]{}()"

############################################################################
# Ausgabe vorbereiten
#print(columns2)
#print(columns)

print ("Hier kommt der Original-String nach Eingabe:\n")

print(teststring)
#print(columns2)
#print(columns)

print ("dieser beinhaltet folgende Anzahl pro Sonderzeichen:")

#######################################
# Aufzählungen aufbereiten
startx = "Sonderzeichen"
footerx = "ist so oft vertreten"
delmitter = ':'
print(columns2)
print(columns)
sani4 = teststring
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten




####################################################################################################
# anzahl Klammern ausgeben
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten

#print(columns2)
#print(columns)
print("es sind " + str(len (klammern)) + " erfasst und zu bereinigen")
print("es sind " + str(len(sonderzeichen)) + startx + " erfasst und zu bereinigen")

#zählen für die liste am ende
#gesamtklammern = str(len(klammern))
#gesamtsonderz = str(len(sonderzeichen))
#gesamtleer = str(len(leerzeichen))
#gesamtumbr = str(len(zeilenumbruch))


schleife = 1
sondercount = 0
abbruch = len(sonderzeichen)

while schleife <= abbruch:
    vszs = schleife - 1
    charx = sonderzeichen[vszs]            #
    countx = sani4.count(charx)         # dies ist eine zahl vom typ integer
    sondercount = sondercount + countx  #
    countxstr = str(countx)             # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')      # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')    # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(5, ' ')
    out = startx + charx + footerx + delmitter + countxstr # ausgabestring zusammensetzen
    print(out)                          # den fertigen ausgabesting ausgeben
    schleife += 1


abbruch2 = len(klammern)
schleife2 = 1
while schleife2 <= abbruch2:
    vszk = schleife2 - 1
    charxk = klammern[vszk]  #
    countx = sani4.count(charxk)  # dies ist eine zahl vom typ integer
    sondercount = sondercount + countx  #
    countxstr = str(countx)  # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')  # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')  # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(5, ' ')
    out = startx + charxk + footerx + delmitter + countxstr  # ausgabestring zusammensetzen
    print(out)  # den fertigen ausgabesting ausgeben
    schleife2 += 1

abbruch3 = len(leerzeichen)
schleife3 = 1
while schleife3 <= abbruch3:
    vszl = schleife3 - 1
    charxl = leerzeichen[vszl]  #
    countx = sani4.count(charxl)  # dies ist eine zahl vom typ integer
    sondercount = sondercount + countx  #
    countxstr = str(countx)  # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')  # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')  # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(5, ' ')
    out = startx + charxl + footerx + delmitter + countxstr  # ausgabestring zusammensetzen
    print(out)  # den fertigen ausgabesting ausgeben
    schleife3 += 1

abbruch4 = len(zeilenumbruch)
schleife4 = 1
while schleife4 <= abbruch4:
    vszz = schleife4 - 1
    charxz = zeilenumbruch[vszz]  #
    countx = sani4.count(charxz)  # dies ist eine zahl vom typ integer
    sondercount = sondercount + countx  #
    countxstr = str(countx)  # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')  # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')  # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(5, ' ')
    out = startx + charxz + footerx + delmitter + countxstr  # ausgabestring zusammensetzen
    print(out)  # den fertigen ausgabesting ausgeben
    schleife4 += 1

###################################################################################################
# Grundsätzliche Bearbeitung zu Eingabefehlern und Bösen Eingabe Anfängen und Enden!
print(columns2)
print(columns)

print("Basisbearbeitung des Strings ")
#Leerzeichen am Anfang und Ende, sicher entfernen
sani1 = teststring.strip(leerzeichen)
sani1 = sani1.replace(zeilenumbruch[0]," ")
sani1 = sani1.replace(zeilenumbruch[1]," ")
sani1 = sani1.replace(leerzeichen[1]," ")

print('Um Leerzeichen Bereinigter String 1:\n' + sani1)

#Klammern am Anfang und Ende entfernen !
sani2 = sani1.strip(klammern)
print('Um Klammern Bereinigter Text 2:\n' + sani2)

# Klammern und Leerzeichen am Anfang und Ende entfernen
sani3 = sani2.strip(klammern)
print('Um Klammern und Leerzeichen Bereinigter Text 3:\n' + sani3)

# Sonderzeichen für Programmierung am Ende entfernen!
# String 3 weiterverarbeiten
sani4 = sani3.strip(sonderzeichen)
print('Um SonderzeichenBereinigter Text 4\n' + sani4)





###################################################################################################
# Durchführung der Bereinigung
print(columns2)
print(columns)
print("Stringinterne Bereinigung um Sonderzeichen.")
schleife2 = 1
abbruch4 = len(sonderzeichen)
while schleife2 <= abbruch4:
    vsz = schleife2 - 1
    sani4 = sani4.replace(sonderzeichen[vsz], " ")
    schleife2 += 1

#sani5 = sani4.replace(sonderzeichen[0]," ")
#sani5 = sani5.replace(sonderzeichen[1]," ")
#sani5 = sani5.replace(sonderzeichen[2]," ")
#sani5 = sani5.replace(sonderzeichen[3]," ")
#sani5 = sani5.replace(sonderzeichen[4]," ")
#sani5 = sani5.replace(sonderzeichen[5]," ")
#sani5 = sani5.replace(sonderzeichen[6]," ")
#sani5 = sani5.replace(sonderzeichen[7]," ")
#sani5 = sani5.replace(sonderzeichen[8]," ")
#sani5 = sani5.replace(sonderzeichen[9]," ")
#sani5 = sani5.replace(sonderzeichen[10]," ")
#sani5 = sani5.replace(sonderzeichen[11]," ")
##sani5 = sani5.replace(sonderzeichen[12]," ")
#sani5 = sani5.replace(sonderzeichen[13]," ")
#sani5 = sani5.replace(sonderzeichen[14]," ")

print("Stringinterne Bereinigung von Klammern.")

schleife3=1
abbruch5= len(klammern)
while schleife3 <= abbruch5:
    vsz = schleife3 - 1
    sani4 = sani4.replace(klammern[vsz], " ")
    schleife3 += 1


#sani5 = sani5.replace(klammern[0]," ")
#sani5 = sani5.replace(klammern[1]," ")
#sani5 = sani5.replace(klammern[2]," ")
#sani5 = sani5.replace(klammern[3]," ")
#sani5 = sani5.replace(klammern[4]," ")
#sani5 = sani5.replace(klammern[5]," ")
#sani5 = sani5.replace(klammern[6]," ")
#sani5 = sani5.replace(klammern[7]," ")

print("Stringinterne Bereinigung von Zeilenumbrüchen.")

schleife4 = 1
abbruch6 = len(zeilenumbruch)
while schleife4 <= abbruch6:
    vsz = schleife4 - 1
    sani4 = sani4.replace(klammern[vsz], " ")
    schleife4 += 1
#sani5 = sani5.replace(zeilenumbruch[0]," ")
#sani5 = sani5.replace(zeilenumbruch[1]," ")
#sani5 = sani5.replace(zeilenumbruch[2]," ")
#sani5 = sani5.replace(klammern[3]," ")
#sani5 = sani5.replace(klammern[4]," ")
#sani5 = sani5.replace(klammern[5]," ")
#sani5 = sani5.replace(klammern[6]," ")
#sani5 = sani5.replace(klammern[7]," ")
####################################################################################################
# Schlussendliche Ausgabe
#print(columns2)
#print(columns)

# noch einmal führende leerzeichen entfernen
#sani5 = sani5.lstrip(' ')
#print(sani5)
print('um Leerzeichen, Sonderzeichen und Klammern Bereinigter Text ')
print('x->:' + sani4.capitalize())
gesamtcount = []
gesamtcount.append(gesamtklammern)
gesamtcount.append(gesamtsonderz)
gesamtcount.append(gesamtleer)
gesamtcount.append(gesamtumbr)
print(gesamtcount)

print

