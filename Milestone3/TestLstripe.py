#mit lstrip() kann man leerzeichen entfernt werden
#mit lstrip() für left = links
#mit lstrip('1234567890!"§$ABCDE) kann man auch gezielte Zeichen links entfernen
#strip() entfernt links als auch rechts zeichen
#rstip() entfernt nur rechts zeichen

#lstrip links
columns='123456789012345678901234567890123456789012345678901234567890123456789'
print(columns)
lstripbeispiel='      leerzeichen ist vorne'
print(lstripbeispiel)
print(lstripbeispiel.lstrip())
