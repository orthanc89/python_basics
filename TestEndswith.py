#endswith

print("mit der methode .endswith kannst du daten/websides etc auf ihre richtige endung überprüfen")

seite = input("bitte geb hier eine Adresse einer Webside ein um diese zu Überprüfen, ob diese auf .de endet. ")

ergebnis=seite.endswith(".de")
print("Wenn die Seite mit .de endet, bekommst du hier ein TRUE aus. wenn nicht, ein FALSE")
print(ergebnis)