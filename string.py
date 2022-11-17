nev=input("Kérek egy nevet: ")

print("A " + nev + " nevet írtad be.")

print("A {belsoNev} nevet írtad be.".format(belsoNev=nev))


if len(nev)<5:
    print("Jó rövid név.")
elif len(nev)>=10: 
    print("Veri big név.")

be="nemvégjel"
szavak=[]
while be!="":
    be=input("írj be valamit: ")
    szavak.append(be)

#szavak.remove("")
#szavak.pop(-1)
#szavak.pop(len(szavak)-1)
#szavak=szavak[:-1]
szavak=[x for x in szavak if x!=""]

print(szavak)
