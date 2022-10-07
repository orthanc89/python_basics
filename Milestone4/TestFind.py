#der Find befehl

eingabe = input("Bitte geb hier einen Satz ein")
print("\n\n")
print("zu beachten: der befehl .find nur den ersten erfolgreichen Treffer aus. Leerzeichen werden mitgezählt. Python fängt bei 0 an zu zählen ")
suche = input("Bitte geb hier ein, was in deinen Satz gefunden werden soll. ")
print eingabe
print(eingabe.find(suche))