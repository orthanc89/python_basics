#title test

print(".title gibt ändert jeden Anfangsbuchstaben in die  Großschreibweise, egal, ob das Wort groß oder klein geschrieben wird.")
eingabe = input("Bitte geb hier einen Text ein, dessen Schreibweise geändert werden soll. Bitte beachte, nicht alle Buchstaben und Zeichen können umgewandelt werden, wie zum Beispiel ß  ")
print("\n\n\n")
print("Hier ein Bisschen Python Zauberkraft")
print("\n\n\n")
print("Deine Eingabe war: " + eingabe)
print("alles kleingeschreiben mit .lower: " + eingabe.lower())
print("\n")
print("alles GROßGESCHRIEBEN mit .upper: " + eingabe.upper())
print("\n")
print("jetzt alles getauscht: " + eingabe.swapcase())
print("\n")
print("jetzt mit casefold: " + eingabe.casefold())
print("\n")
print("jetzt mit .title geändert: " + eingabe.title())

