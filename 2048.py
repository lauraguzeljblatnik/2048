import random

igra = [['','','',''],['','','',''],['','','',''],['','','','']]

class Plosca:
    def __init__(self, vsota=0):
        self.vsota = random.choice('24')

    def premik(self):
        if klik == 'levo':
            for i in range(0,3):
                if [i][y+1] == '':
                    igra [x][y+1] = y
                    igra [x][y] = ''
