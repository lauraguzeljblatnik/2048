# projektna naloga

import tkinter as tk
import 2048

class Plosca:
    def __init__(self, okno):

    def obdelaj_tipko(self, event):
        if event.keysym == 'Right':
            self.2048.stisni_desno(A)
        elif event.keysym == 'Left':
            self.2048.stisni_levo(A)
        elif event.keysym == 'Up':
            self.2048.stisni_gor(A)
        elif event.keysym == 'Down':
            self.2048.stisni_dol(A)



okno = tk.Tk()
okno.mainloop()
