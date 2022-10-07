#
#
#replace befehl
eingabe = input("Bitte geb hier einen Text ein")
print("\n")
eingabe1 = input("Gib hier ein Wort aus deinem vorherigen Text ein, welches ersetzt werden soll")
print("\n\n")
ersatz = input("geb hier das ein, mit dem ersetzt werden soll")
out = eingabe.replace(eingabe1, ersatz)
print("\n\n")
print(out)