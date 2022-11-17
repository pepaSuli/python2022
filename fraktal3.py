import matplotlib.pyplot as plt

def haromszog(pontok,elozmeny, melyseg=1):
    #print("Pontok")
    #print(pontok)
    #print("Pontok vége")
    A=pontok[0]
    B=pontok[1]
    C=pontok[2]

    if melyseg>0:
        AB=[0,0]
        AC=[0,0]
        BC=[0,0]

        AB[0]=(A[0]+B[0])/2
        AB[1]=(A[1]+B[1])/2
        AC[0]=(A[0]+C[0])/2
        AC[1]=(A[1]+C[1])/2
        BC[0]=(B[0]+C[0])/2
        BC[1]=(B[1]+C[1])/2

        uj1=haromszog([A,AB,AC],elozmeny, melyseg-1)
        uj2=haromszog([AB,B,BC],elozmeny, melyseg-1)
        uj3=haromszog([AC,BC,C],elozmeny, melyseg-1)
    else:
        elozmeny+=[[A,B,C]]

    return elozmeny

lista=haromszog([[0,0],[100,0],[50,50]],[],7)
print(len(lista))

for egy in lista:
    x=[]
    y=[]
    for p in egy:
        x.append(p[0])
        y.append(p[1])
    x.append(egy[0][0])
    y.append(egy[0][1])

    plt.plot(x,y)

plt.show()


