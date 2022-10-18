

#modul import
import re
#If abfrage und boolsche variable

#
print("\n\n\n")
variax = input("Bitte geb etwas ein.")

#grundvariablen definieren
zahler = 0
buchstabe = 0
zeichen = 0
zahlen= 0
grbuch = 0
kleinbuch = 0
sonderz = 0

# zahlen zählen
zahlen = re.findall(r"[0-9]", variax)

# buchstaben zählen
grbuch = re.findall(r"[A-Z]", variax)
kleinbuch = re.findall(r"[a-z]", variax)

# sonderzeichen zählen
sonderz = re.findall(r"[%$§\"`*<>\[_|\]{}()#+'/:;-]", variax)

for len(nummernel) in variax:
    zahlen += 1

for len(grbuch) in variax:
    buchstabe += 1

for len(kleinbuch) in variax:
    buchstabe += 1

for len(sonderz) in variax:
    zeichen += 1

if (zeichen == 0 and zahlen >=1 and buchstabe ==0):
    print("du hast nur zahlen eingegeben")

if (zeichen == 0 and zahlen ==0 and buchstabe >= 1):
    print("du hast nur Buchstaben eingegeben")

if (zeichen >= 1 and zahlen ==0 and buchstabe == 0):
    print("du hast nur Sonderzeichen eingegeben")

if (zeichen >= 1 and zahlen >= 1 and buchstabe == 0):
        print("du hast Sonderzeichen und Zahlen eingegeben")

if (zeichen == 0 and zahlen >= 1 and buchstabe >= 1):
        print("du hast Buchstaben und Zahlen eingegeben")

if (zeichen >= 1 and zahlen >= 1 and buchstabe >= 1):
            print("du hast Sonderzeichen und Zahlen und Buchstaben eingegeben")