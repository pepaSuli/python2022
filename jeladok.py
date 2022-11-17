import math

def eltelt(kezd,veg):
    s=masodperc(veg)-masodperc(kezd)
    return str(s//3600).ljust(2,"0")+":"+str(s%3600//60).ljust(2,"0")+":"+str(s%60).ljust(2,"0")
def elteltS(kezd,veg):
    return masodperc(veg)-masodperc(kezd)

def masodperc(ido):
    return int(ido[0])*60*60+int(ido[1])*60+int(ido[2])

def tav(k1,k2):
    return math.sqrt((k1[0]-k2[0])**2+(k1[1]-k2[1])**2)

f=open("jel.txt")
teljes=f.read()
f.close()
print(teljes)

lista=[e.split(" ") for e in teljes.split("\n")][:-1]

print("2. feladat")
sorszam=int(input("Adja meg a jel sorszámát! "))
print("x={} y={}".format(lista[sorszam-1][3],lista[sorszam-1][4]))

print("4. feladat")
print("Időtartam: "+eltelt(lista[0],lista[-1]))

print("5. feladat")
x_ek=[int(e[3]) for e in lista ]
y_ok=[int(e[4]) for e in lista ]

print("Bal alsó: {} {}, jobb felső: {} {}".format(min(x_ek),min(y_ok),max(x_ek),max(y_ok)))

print("6. feladat")
pontok=[list(map(int,e)) for e in lista]

tavok=[tav(pontok[i],pontok[i+1]) for i in range(0,len(pontok)-1)]
print("Elmozdulás: {0:0.3f} egység".format(sum(tavok)))

print("7. feladat")
idoelteres=[ i for i in range(0,len(lista)-1) if elteltS(lista[i][:3],lista[i+1][:3])>300]
xyelteres=[ i for i in range(0,len(lista)-1) if abs(int(lista[i][3])-int(lista[i+1][3]))>10 or abs(int(lista[i][4])-int(lista[i+1][4]))>10]
#print(xyelteres)

elteresek=[]
f=open("kimaradt.txt","w")
for i in range(0,len(lista)-1):
    szoveg=""
    if elteltS(lista[i][:3],lista[i+1][:3])>300:
        szoveg="{} {} {} időeltérés {}".format(lista[i][0],lista[i][1],lista[i][2],elteltS(lista[i][:3],lista[i+1][:3])//300)
    elif abs(int(lista[i][3])-int(lista[i+1][3]))>10 :
        szoveg="{} {} {} koordináta-eltérés {}".format(lista[i][0],lista[i][1],lista[i][2],abs(int(lista[i][3])-int(lista[i+1][3]))//10)
    elif abs(int(lista[i][4])-int(lista[i+1][4]))>10 :
        szoveg="{} {} {} koordináta-eltérés {}".format(lista[i][0],lista[i][1],lista[i][2],abs(int(lista[i][4])-int(lista[i+1][4]))//10)

    if szoveg!="":
        f.write(szoveg+"\n")
f.close()        
