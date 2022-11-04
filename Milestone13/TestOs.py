#bitte ebook seite 179-189 durcharbeiten:
# hierzu bitte das OS MOdul importieren und
# 1. euer Homeverzeichnis auflisten lassen,
# 2. nur alle Verzeichnisse in eurem Homeverzeichnis auflisten lassen
# 3. euren Loginnamen/usernamen anzeigen lassen
# 4. die Betriebsystemart auflisten lassen



import os

user = input('Bitte geb deinen Namen ein: ')

systemname = os.name

if systemname == "nt":
    systemname = "Windows"
if systemname == "posix":
    systemname = "Linux/Unix/Mac"

print(os.environ)

print('Hey, ' + user + ", du benutzt ein: " + systemname + ' System')
print("\n")
print(user + ', das sind deine "Arbeitsverzeichnis" lautet:')
print(print(os.getcwd()))
print("\n")
home =os.getenv('HOMEDRIVE')
print(user + ", dein Homeverzeichnis lautet: " + home)
print("Das sind alle unterordner in deinem Home Verzeichnis")
print(os.listdir(os.getenv('HOMEDRIVE')))
print
login = os.getenv('USERNAME')
print(user + ", Dein Username lautet: " + login)

