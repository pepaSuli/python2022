import copy

class MyClass:
    x=5
    def megnovel(self,mennyivel=2):
        self.x+=mennyivel


class kutya:
    nev,fajta,agresszivitas,kor,szin=["","",0,0,""]
    def __init__(self,nev,fajta,agresszivitas,kor,szin):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitas=agresszivitas
        self.kor=kor
        self.szin=szin

    def ugat(self):
        print("Vau-vau")

    def koszon(self):
        print("Vau-vau, {} vagyok".format(self.nev))

    def talalkozas(self,masik):
        if self.agresszivitas>5 or masik.agresszivitas>5:
            #támadás
            if self.agresszivitas>=masik.agresszivitas:
                print("Megöllek, kutya!")
            else:
                print("Ne bánts, báttya!")
        else:
            if self.agresszivitas>=masik.agresszivitas:
                print("Szevasz, kutya!")
            else:
                print("Szia, báttya!")       

k1=kutya("Bodri","puli",3,9,"fekete")
k2=kutya("Morzsi","golden retriver",1,3,"világos barna")

k1.ugat()
k1.koszon()
k2.koszon()

k2.talalkozas(k1)
k1.talalkozas(k2)




"""    
print(MyClass.x)

p1=MyClass()
print(p1.x)
p2=MyClass()
p2.x=1
print(p2.x)

p1.megnovel()
p1.megnovel(10)
print(p1.x)
"""









