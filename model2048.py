import random

def stisni_vrstico_levo(A):
#vse elemente v vrsrici stisne v levo
    B = []
    for i in range(len(A)):
        if A[i] != 0:
            B += [A[i]]
    if B == []:
        B = B
    elif len(B) == 1:
        B = B
    elif B[0] != B[1]:
        B = [B[0]] + stisni_vrstico_levo(B[1:])
    elif B[0] == B[1]:
        B = [2*B[0]] + stisni_vrstico_levo(B[2:])
    nicle = len(A) - len(B)    
    return B + nicle*[0]

def stisni_levo(A):
# kot argument vzame matriko A in vrne matriko, ki ima vse stisnjeno v levo
    B = []
    for i in range(4):
        B.append (stisni_vrstico_levo(A[i]))
    return B

def stisni_vrstico_desno(A):
#vse elemente v vrsrici stisne v desno
    B = stisni_vrstico_levo(A[::-1])
    return B[::-1]

def stisni_desno(A):
# kot argument vzame matriko A in vrne matriko, ki ima vse stisnjeno v desno
    B = []
    for i in range(4):
        B.append( stisni_vrstico_desno(A[i]))
    return B

def stisni_gor(A):
# kot argument vzame matriko A in vrne matriko, ki ima vse stisnjeno gor
    B = [[],[],[],[]]
    for j in range(4):
        stolpec = []
        for i in range(4):
            stolpec.append(A[i][j])
        stolpec = stisni_vrstico_levo(stolpec)
        for i in range (4):
            B[i].append(stolpec[i])
    return B

def stisni_dol(A):
# kot argument vzame matriko A in vrne matriko, ki ima vse stisnjeno dol
    B = [[],[],[],[]]
    for j in range(4):
        stolpec = []
        for i in range(4):
            stolpec.append(A[i][j])
        stolpec = stisni_vrstico_desno(stolpec)
        for i in range (4):
            B[i].append(stolpec[i])
    return B

def vstavi_novo_stevilko(A):
#funkcija nakljucno postavi stevilo 2 ali 4 v matriko
    nicle = 0
    for j in range(4):
        for i in range(4):
            if A[i][j] == 0:
                nicle += 1
    if nicle == 0:
        return A

    B = []
    for i in range(4):
        vrstica = []
        for j in range(4):
            vrstica.append(A[i][j])
        B.append(vrstica)

    i = random.randint(0,3)
    j = random.randint(0,3)

    while B[i][j] != 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
    B[i][j] = int(random.choice('24'))
    return B

  
