#strip links und rechts
columns='123456789012345678901234567890123456789012345678901234567890123456789'
print("alle unerwünschten leerzeichen entfernen mit strip()")
print("\n")
print(columns)
beispiel="       Bockwurst ist lustig eine Bockwurst ist schön     "
print(beispiel)
ausgabe=beispiel.strip()
print(ausgabe)

print("\n\n")

#und jetzt etwas schwieriger

print("Bitte geb eine Zeichenfolge ein. mach zu erst Sonderzeichen und Zahlen und dann dein Wort/Buchstaben und dann wieder Sonderzeichen & zahlen")

#string1 = input("bitte hier was eingeben, wie oben beschrieben")

string1 = "!§$151bockwurst51781"
ausgaben = string1.strip('0123456789')

# ausgaben2 = ausgaben.stripe('!"%$')

sonderzeichen = "!\"§$%&/()=?²³{[]}\\´`"
zahlen = "0123456789"

ausgabe3 = ausgaben.strip(sonderzeichen)
ausgabe4 = ausgabe3.strip(zahlen)

print(ausgabe4)

