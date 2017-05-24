import random

igra = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

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
    for i in range(0,4):
        A[i] = stisni_vrstico_levo(A[i])

def stisni_vrstico_desno(A):
#vse elemente v vrsrici stisne v desno
    B = stisni_vrstico_levo(A[::-1])
    return B[::-1]

def stisni_desno(A):
# kot argument vzame matriko A in vrne matriko, ki ima vse stisnjeno v desno
    for i in range(0,4):
        A[i] = stisni_vrstico_desno(A[i])

def stisni_gor(A):
    for j in range(0,4):
        vrstica = []
        for i in range(4):
            vrstica.append(A[i][j])
        B = stisni_vrstico_levo(vrstica)
        for i in range (4):
            A[i][j] = B[i]
    return (A)

def stisni_dol(A):
    for j in range(0,4):
        vrstica = []
        for i in range(4):
            vrstica.append(A[i][j])
        B = stisni_vrstico_desno(vrstica)
        for i in range (4):
            A[i][j] = B[i]
    return (A)

A = [0,4,8,2,2,2,0,0,0,0]
C = [[4,2,2,0],[0,0,0,4],[2,0,0,0],[2,0,0,0]]
