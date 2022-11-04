# 5. mit der Datefunktion das aktuelle datum anzeigen lassen
# 6. mit der Date-Funktion die aktuelle Uhrzeit anzeigen lassen
# 7. die/das Datum und die Urzeit in europäischer und in amerikanischer Schreibweise anzeigen lassen.
import locale
from datetime import date
from datetime import time
from datetime import timezone

locale.setlocale('de_DE')

aktuellesDatum = date.today()
print("Deutsches Format: " + aktuellesDatum.strftime("%A %B %d.%m.%Y"))
print("Englisches Format: " + aktuellesDatum.strftime("%m.%d.%Y"))

#print(dir(time))
aktuelleZeit = time.now('hour')
#print("Aktuelle Uhrzeit: " + aktuelleZeit.strftime("%X %x %H.%M.%S %Z"))



