

import re
from urllib import request

putput = input("Geb hier bitte ine webside zum scannen ein: ")
rueckgabewert = request.urlopen(putput)
print(type(rueckgabewert))

rueckgabewert = request.urlopen(putput)
print(rueckgabewert.code)
print("Dateigröße in Bytes: ", rueckgabewert.length)
print("Anfang des Inhalts:", rueckgabewert.peek())
inhalt = rueckgabewert.read()
print(type(inhalt))

# hier ggf. harte fehlerbehandlung einbauen für den fall das eine webside einen codeerror aufruft
decodex = re.findall("charset=")

inhalt_text = inhalt.decode("UTF-8")
print(type(inhalt_text))
inhalt_text = inhalt.decode("UTF-8")
print(inhalt_text)