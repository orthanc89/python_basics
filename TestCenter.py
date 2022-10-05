#center befehl
from time import sleep


#columns basten
#colum1 = int(column1)
#column = int(colum2)
column1 = '0000000000111111111122222222223333333333444444444455555555556666666666'
column2 = '0123456789012345678901234567890123456789012345678901234567890123456789'
print("So liebe Leute, willkommen bei der zauberhaften Zauberwelt von Python.")
print("\n\n")
sleep(1)
wort = input("Bitte gebe doch mal ein Wort ein")
zeichen = input("Jetzt möchte ich von dir noch ein Sonderzeichen haben.Sonderzeichen sind: §$%&/()=?!{[]}\#+*~' ")
zahl = input ("jetzt bitte eine Zauberzahl")
zahl = int(zahl)
print("\n\n\n")
print("jetzt lass mich mal machen.. ich bin nicht mehr der jüngste!*hust hust*")
print("\n\n")
sleep(1)
print("So jetzt ja. ")

########
out1 = wort.ljust(zahl, zeichen)
out2 = wort.center(zahl, zeichen)
out3 = wort.rjust(zahl, zeichen)

#####
print("OOOOOOOHHHHHHHHHHHHHHHHHHHHHHHHHHHHMMMM")
sleep(2)
print("OOOOOOOHHHHHHHHHHHHHHHHHHHHHHHHHHHHMMMM")
sleep(1)
print("Bei der Macht der heiligen Bockwurst")
sleep(1)
print(out1 + out3)
sleep(1)
print(out2 + out2)
sleep(1)
print(out3 + out3)
sleep(1)
print(out2 + out2)
sleep(1)
print(out1 + out1)
sleep(1)
print("Müde ich bin.. Lernen du noch viel hat, junger Padawan. Live long and Prosper \' \\\\//,\' ")
