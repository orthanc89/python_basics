import tkinter
import sys

import tkinter as tk


root = tk.Tk()


def beenden():
    print("Tschüßikowsky")



def benutzeranlegen():
    #vname
   # nname
    #alter
    #telnr
    #password
   # passwordx
    vname_wert = tk.StringVar()
    vname = tk.Entry(root, textvariable=vname_wert)
    vname.grid(row=2, column=2)
    vorname = tk.Label(root, text="Vorname:",font='Comic-Sans-MS')
    vorname.grid(row=2, column=1)

    nname_wert = tk.StringVar()
    nname = tk.Entry(root, textvariable=nname_wert)
    nname.grid(row=3, column=2)
    nachname = tk.Label(root, text="Nachname:",font='Comic-Sans-MS')
    nachname.grid(row=3, column=1)

    alter_wert = tk.StringVar()
    alter = tk.Entry(root, textvariable=alter_wert)
    alter.grid(row=4, column=2)
    alter = tk.Label(root, text="Alter:",font='Comic-Sans-MS')
    alter.grid(row=4, column=1)

    telnr_wert = tk.StringVar()
    telnr = tk.Entry(root, textvariable=telnr_wert)
    telnr.grid(row=5, column=2)
    telnr = tk.Label(root, text="Telefonnummer:",font='Comic-Sans-MS')
    telnr.grid(row=5, column=1)

    userpw_wert = tk.StringVar()
    userpw = tk.Entry(root, textvariable=userpw_wert, show="*")
    userpw.grid(row=6, column=2)
    userpw = tk.Label(root, text="Benutzerpasswort:",font='Comic-Sans-MS')
    userpw.grid(row=6, column=1)

    leerzeile = tk.Label(root, text="").grid(row=7, column=1)

    passswdfeld_wert = tk.StringVar()
    passswdfeld = tk.Entry(root, textvariable=passswdfeld_wert, show="*")
    passswdfeld.grid(row=8, column=2)
    passwd = tk.Label(root, text="Password für eintrag ändern:",font='Comic-Sans-MS')
    passwd.grid(row=8, column=1)

    passswdfeldwdh_wert = tk.StringVar()
    passswdfeldwdh = tk.Entry(root, textvariable=passswdfeld_wert, show="*")
    passswdfeldwdh.grid(row=9, column=2)
    passwdwdh = tk.Label(root, text="Passwort wiederholen:", font='Comic-Sans-MS')
    passwdwdh.grid(row=9, column=1)



    schaltfl1 = tk.Button(root, text="Enter").grid(row=12, column= 1)
    schaltfl2 =tk.Button(root, command=beenden(), text="Beenden").grid(row=12, column=2)



ausgewaehlt = tk.StringVar()
#anrede wählen
def chooseanrede():
    anrede = ['Männlein', 'Weiblein', 'Salatgurke']
    ausgewaehlt.set('Weiblein')


    for einzellwert in anrede:
        radiobutton = tk.Radiobutton(root, text=einzellwert, value=einzellwert, variable=ausgewaehlt)
        radiobutton.pack()


#mainprogramm

chooseanrede()
print(ausgewaehlt.get())

#benutzeranlegen()
root.mainloop()