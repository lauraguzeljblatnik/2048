# projektna naloga

import tkinter as tk

okno = tk.Tk()

#igra = tk.Frame(okno)
#igra.grid(row=0, column=0)

#gumbi = tk.Frame(okno)
#gumbi.grid(row=0, column=1)
#gor = tk.Button(gumbi, text='↑')
#gor.grid(row=0, column=1)
#levo = tk.Button(gumbi, text='←')
#levo.grid(row=1, column=0)
#dol = tk.Button(gumbi, text='↓')
#dol.grid(row=1, column=1)
#desno = tk.Button(gumbi, text='→')
#desno.grid(row=1, column=2)

igralna_plosca = tk.Frame(okno)
igralna_plosca = tk.Canvas(okno, width=500, height=500)



okno.mainloop()
