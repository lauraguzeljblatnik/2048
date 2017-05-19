import tkinter as tk

okno = tk.Tk()

crte = tk.Canvas(okno, width=200, height=100)
crte.pack

crte.create_line(0, 0, 200, 100)

okno.mainloop()
