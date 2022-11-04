


import tkinter as tk


root = tk.Tk()
#textausgabe erzeugen

label1 = tk.Label(root, text='Hallo welt')
label1.pack()

label2 = tk.Label(root, text="Hier kommt gleich eine Biene",
                  fg='#2B32A3', #fordergrundfarbe
                  bg='#FFE999', #background colour
                  font=('comic', #schriftart
                        35,
                        'bold'))
label2.pack()

bild1 = tk.PhotoImage(file ='biene.png')

label= tk.Label(root, image=bild1).pack()


root.mainloop()