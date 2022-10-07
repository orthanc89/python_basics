#zfill test

eingabe = input("Bitte geb hier etwas ein, dass durch .zfill am anfang erweiter werden soll. Es bieten sich hier positive, Natürliche Zahlen an")
print("\n")
stelle = input("Bitte geb hier an, auf wieviele stellen deine Eingabe erweitert werden soll.")
stelle = int(stelle)
out = eingabe.zfill(stelle)
print("\n")
print(out)