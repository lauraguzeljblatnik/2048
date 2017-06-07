# projektna naloga

import tkinter as tk
import tkinter.messagebox
import igra2048 

class Plosca:
    def __init__(self, okno):
        self.slika = tk.Canvas(okno, width = 200, height = 200)
        self.slika.place(x= 20, y= 20)
        self.gumb_nova_igra = tk.Button(
            okno,
            text = 'Nova igra',
            command = self.nova_igra
            )
        self.gumb_nova_igra.place(x = 250, y = 20)
        self.napis = tk.Label (okno, text = 'Tocke :')
        self.napis.place(x = 250, y= 50)
        okno.bind('<Key>', self.obdelaj_tipko)

    def nova_igra(self):
        self.matrika = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        igra2048.vstavi_novo_stevilko(self.matrika)
        self.narisi()
        

    def narisi_polje(self, i, j):
        if self.matrika[i][j] != 0: 
            self.slika.create_text(
                50*j + 25,
                50*i +25,
                text = str(self.matrika[i][j])
                )
        

    def narisi(self):
        self.slika.delete('all')
        for i in range(4):
            for j in range(4):
                self.narisi_polje(i, j)
        

    def obdelaj_tipko(self, event):
        A = self.matrika
        if event.keysym == 'Right':
            B = igra2048.stisni_desno(A)
        elif event.keysym == 'Left':
            B = igra2048.stisni_levo(A)
        elif event.keysym == 'Up':
            B = igra2048.stisni_gor(A)
        elif event.keysym == 'Down':
            B = igra2048.stisni_dol(A)
        else:
            return None
        
        self.matrika = B
        igra2048.vstavi_novo_stevilko(B)
        self.narisi()

        if (
            B == igra2048.stisni_levo(B) and
            B == igra2048.stisni_desno(B) and
            B == igra2048.stisni_gor(B) and
            B == igra2048.stisni_dol(B) 
            ):

            tkinter.messagebox.showinfo("Say Hello", "Zgubil si!")

        for i in range(4):
            for j in range(4):
                if B[i][j] == 2048:
                    print('zmagaaaa!')
            
            

        
            igra2048.vstavi_novo_stevilko(B)

    



okno = tk.Tk()



igra = Plosca(okno)

okno.mainloop()

