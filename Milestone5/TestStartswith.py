#startswith

print("Mit der Methode .startswith kann man, ähnlich der endswith, Seiten/DAten udn der gleichen auf den richtigen  Beginn überprüfen.")

seite=input( "Bitte geb eine FQDN [vollständige WEb-Adresse mit http:// bzw. https://] ein und das Programm schaut nach, ob die SEite mit https:// anfängt")

print("Wenn die Seite mit http:// anfängt bekommst du ein False, wenn nicht, ein True")

ergebnis=seite.startswith('https://')
print(ergebnis)