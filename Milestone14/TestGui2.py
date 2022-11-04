


import tkinter
import sys

import tkinter as tk
root = tk.Tk()

def beenden():
    print("Tschüßikowsky")

def benutzeranlegen():
    vname
    nname
    alter
    telnetlibemail
    password
    passwordx



def passworteingabe():

    eingabefeld_wert = tk.StringVar()
    eingabefeld = tk.Entry(root, textvariable=eingabefeld_wert)
    eingabefeld.grid(row=3, column=1)
    eingabefeld_wert.set("Hier ist der Text als STR")
    username = tk.Label(root, text="Usersanme:")
    username.grid(row=3, column=0)

    passswdfeld_wert=tk.StringVar()
    passswdfeld=tk.Entry(root, textvariable=passswdfeld_wert, show="*")
    passswdfeld.grid(row = 4, column= 1)
    passwd = tk.Label(root, text="Password:")
    passwd.grid(row=4, column=0)

    schaltfl1 = tk.Button(root, text="Enter").grid(row=5, column= 1)
    schaltfl2 =tk.Button(root, command=beenden(), text="Beenden").grid(row=5, column=2)


passworteingabe()
root.mainloop()