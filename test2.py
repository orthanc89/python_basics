import re
ip_str = input("Geben Sie den String ein: ")
# Verwendung von re.findall()
ucase = re.findall(r"[AZ]", ip_str)
lcase = re.findall(r"[az]", ip_str)
specialc = re.findall(r"[,.!?]", ip_str)
numc = re.findall(r"[0-9]", ip_str)
print("Anzahl der Großbuchstaben: ", len(ucase))
print ("Anzahl der Kleinbuchstaben: ", len(lcase))
print("Anzahl der Sonderzeichen: ", len(specialc))
print("Anzahl der numerischen Zeichen: ", len(numc))
