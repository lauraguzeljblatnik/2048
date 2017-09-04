# projektna naloga

import tkinter as tk
import igra2048
from tkinter import simpledialog
import tkinter.messagebox
from os import startfile


class Plosca:
    def __init__(self, okno):
        self.slika = tk.Canvas(okno, width = 400, height = 400)
        self.slika.place(x= 20, y= 20)
        okno.title('2048')
        okno.geometry("670x500")

        #gumb nova igra
        self.gumb_nova_igra = tk.Button(
            okno,
            text = 'NOVA IGRA',
            command = self.nova_igra,
            width = 12,
            height = 2,
            font = ('Courier', 15, 'bold')
            )
        self.gumb_nova_igra.place(x = 470, y = 50)

        #gumb za seznam zmagovalcev
        self.gumb_zmagovalci = tk.Button(
            okno,
            text = 'ZMAGOVALCI',
            command = self.odpri_seznam_zmagovalcev,
            width = 15,
            font = ('Courier', 12))
        self.gumb_zmagovalci.place(x = 470, y = 150)
        

        okno.bind('<Key>', self.obdelaj_tipko)
        

    #funkcija postavi matriko za novo igro
    def nova_igra(self):
        A = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.matrika = igra2048.vstavi_novo_stevilko(A)
        self.narisi()
        
            
    #funkcija izriše polje in ga pobarva
    def narisi_polje(self, i, j):
        if self.matrika[i][j] == 2:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FFFF66",
                fill = "#FFFF66")

        if self.matrika[i][j] == 4:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FFE55C",
                fill = "#FFE55C")

        if self.matrika[i][j] == 8:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FFCB52",
                fill = "#FFCB52")

        if self.matrika[i][j] == 16:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FFB148",
                fill = "#FFB148")

        if self.matrika[i][j] == 32:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FF973E",
                fill = "#FF973E")

        if self.matrika[i][j] == 64:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FF7D34",
                fill = "#FF7D34")

        if self.matrika[i][j] == 128:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FF632A",
                fill = "#FF632A")

        if self.matrika[i][j] == 256:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FF4920",
                fill = "#FF4920")

        if self.matrika[i][j] == 512:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FF2F16",
                fill = "#FF2F16")

        if self.matrika[i][j] == 1024:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#FF150C",
                fill = "#FF150C")

        if self.matrika[i][j] == 2048:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#F70005",
                fill = "#F70005")

        if self.matrika[i][j] == 4096:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#C70023",
                fill = "#C70023")

        if self.matrika[i][j] == 8192:
            self.slika.create_rectangle(
                (100*j, 100*i, 100*j + 100, 100*i + 100),
                outline = "#C70023",
                fill = "#C70023")
            
        if self.matrika[i][j] != 0:
            self.slika.create_text(
                100*j + 50,
                100*i + 50,
                text = str(self.matrika[i][j]),
                font = ('Arial', 20, 'bold'),
                fill = '#1C1C1C')
                

    #funkcija izriše celotno matriko    
    def narisi(self):
        self.slika.delete('all')
        for i in range(4):
            for j in range(4):
                self.narisi_polje(i, j)
                
        
    #funkcija izvriši zahtevan premik ploščic in vstavi novo ploščico
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
        
        self.matrika = igra2048.vstavi_novo_stevilko(B)
        self.narisi()

    #funkcija sporoči, da je igre konec
        if (
            B == igra2048.stisni_levo(B) and
            B == igra2048.stisni_desno(B) and
            B == igra2048.stisni_gor(B) and
            B == igra2048.stisni_dol(B) 
            ):

            tkinter.messagebox.showinfo("OBVESTILO",
                                        "Zgubili ste! \nVeč sreče prihodnjič!")

    #funkcija vpraša za ime in ga napiše v datoteko
        for i in range(4):
            for j in range(4):
                if B[i][j] == 2048:
                    name = simpledialog.askstring('ČESTITKE!',
                            'Zmagali ste! \n\n Vnesite vaše ime',
                            parent = okno)
                    with open ('zmagovalci.txt', 'a') as winners:
                        print('{}\n'.format(name), file = winners)


    #funkcija odpre datoteko z zmagovalci
    def odpri_seznam_zmagovalcev(self):
        startfile("zmagovalci.txt")
        
    



okno = tk.Tk()

igra = Plosca(okno)

okno.mainloop()

