import numpy as np # necesara pentru vectory (arrays)
import random # pentru generarea numerelor pseudorandom
import math as mt # pentru diverse functii matematice


def numarare(a): 
    n=N
    for i in range (0,n):
        nr = 0
        for j in range(0,n):
            if a[i][j] == 1:
                nr +=1
            else:
                if nr!=0:
                    print("linia, numar+ {},{}".format(i,nr))
                    nr = 0

def suma_vecinilor(spin):
    f = open('C.txt','w')
    C = 0
    Suma = 0
    for x in range (0, N-1):
        for y in range(0,N-1):
            C = spin[x - 1][y] + spin[x + 1][y] + spin[x][y - 1] + spin[x][y + 1]
            Suma += C
            C =0
    print(Suma)
    f.write(str(Suma))
    return Suma

if __name__ == '__main__':
    N = 26
    JJ = 1
    T = 3
    Kb = 1
    NrPasiMontecarlo = 1001
    spin1 = [[1] * N] * N 
    spin = np.array(spin1) # ne vom folosi de un array din biblioteca numpy pentru a fi asemanator cu cel din C
    Sv =0
    Wi = 0
    Wf = 0
    plus =0
    minus =0
    dE = 0
    for j in range (0,N):
        spin[0][j] = 0
        spin[N-1][j] = 0
        spin[j][0] =0
        spin[j][N-1] = 0
    k=0
    for pasiMC in range (0,NrPasiMontecarlo):
        for contor1 in range (0,N*N):
            x = random.randint(1,N-2)
            y = random.randint(1,N-2)
            Sv = spin[x - 1][y] + spin[x + 1][y] + spin[x][y - 1] + spin[x][y + 1]
            dE = 2 * JJ * Sv * spin[x][y]
            P = mt.exp(-dE / T)
            r = random.random()
            if r<P:
                spin[x][y] = -spin[x][y]

    mat = np.matrix(spin)
    with open('Patrat.txt','w') as f:
        for line in mat: # salvam matricea linie cu linie in fisier
            np.savetxt(f, line, fmt='%2d')

    numarare(spin)
    suma_vecinilor(spin)


  