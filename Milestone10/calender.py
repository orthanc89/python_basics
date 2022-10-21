#int =get_days(year ,month)
def get_days(year,month):
    maxdays = 1
    x = []
    short = [4,6,9,11]
    long = [1,3,5,7,8,10,12]
    datum = {'tag':1,'monat':month,'jahr':year}
    if check_schaltjahr(datum) and month == 2:
        # Wir haben ein Schaltjahr
        maxdays = 29
    elif month == 2:
        maxdays = 28

    if month in long:
        maxdays = 31

    if month in short:
        maxdays = 30


    #Liste für die Tage erzeugen
    loop = 1
    while loop <= maxdays:
        x.append(loop)
        loop += 1
    return x

#int =get_months()
def get_months():
    x = []
    loop = 1
    end = 12
    while loop <= end:
        x.append(loop)
        loop += 1
    return x

#int =get_years()
def get_years():
    x = []
    loop = 1900
    end = 2500
    while loop <= end:
        x.append(loop)
        loop += 1
    return x

#check_datum(datum)  # model#  prüfen ob das Datum korrekt eingegeben wurde
def check_datum(datum):
    x = False
    daycount = len(get_days(datum['jahr'], datum['monat']))
    if daycount >= datum["tag"]:
        d = True
    else:
        d = False

    if datum['monat'] <= 12 and datum['monat'] >= 1:
        m = True
    else:
        m = False

    if datum['jahr'] >= 1900 and datum['jahr'] <= 2500:
        j = True
    else:
        j = False

    if d and m and j:
        x = True

    return x

#check_schaltjahr(datum['year'])  #
def check_schaltjahr(datum):
    #x = False
    return not(datum['jahr']%4)

#view_datum(datum)  # view #  usgabe ob datum korrekt ist
def view_datum(datum):
    x = False
    out = "Datum : " + str(datum['jahr']).zfill(4) + "-" + str(datum['monat']).zfill(2) + "-" + str(datum['tag']).zfill(2)
    if check_schaltjahr(datum):
        out += "\n"
        out += "Wir haben ein Schaltjahr im Datum!!!"
    if check_datum(datum):
        out += "\n"
        out += "Datum ist gültig!!!"
    else:
        out += "\n"
        out += "Datum ist ungültig!!!"
    print(out)
    return out

#get_data_from_user_view() # view #  eingabe eines Datums und zerlegen in jahr, monat, tag
def get_data_from_user_view():
    x = False
    inp1 = input('Bitte gib die Zahl für ein Tag ein ! ')
    if inp1.isnumeric():
        xinp1 = int(inp1)
    else:
        xinp1 = 0
    day = xinp1

    inp2 = input('Bitte gib die Zahl für ein Monat ein ! ')
    if inp2.isnumeric():
        xinp2 = int(inp2)
    else:
        xinp2 = 0
    month = xinp2

    inp3 = input('Bitte gib die Zahl für ein Jahr ein ! ')
    if inp3.isnumeric():
        xinp3 = int(inp3)
    else:
        xinp3 = 0
    year = xinp3

    #month = int(input('Bitte gib die Zahl für ein Monat ein ! '))
    #year = int(input('Bitte gib die Zahl für ein Jahr ein ! '))
    datum = {'tag':day,'monat':month, 'jahr':year}
    return datum

# Hier beginnt unser Test Programm
date = get_data_from_user_view()
#print(date)
#print(check_schaltjahr(date))
view_datum(date)
print(get_years())
print(get_months())
print(get_days(date['jahr'],date['monat']))
