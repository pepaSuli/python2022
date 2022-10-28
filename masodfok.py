import math

#a*X2+b*x+c

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

#(-b+gyök(b2-4ac)) / 2a

#print(math.sqrt(3))
diszkriminans=b*b-4*a*c
if diszkriminans<0:
    print("nincs megoldás")
elif diszkriminans==0:
    megoldas=-b /(2*a)
    print("1 megoldás: {}".format(megoldas))
else:
    x1=(-b+math.sqrt(diszkriminans)) / (2*a)
    x2=(-b-math.sqrt(diszkriminans)) / (2*a)
    print("2 megoldás: x1:{}, x2:{}".format(x1,x2))

#gyok=math.sqrt(1)
#print(gyok)

