d1=0.5
d2=0.75
p1=0.75
p2=0.4375

r=1
b=1

p1temp = (1-(1-(1-d1)**r)**b)
p2temp = (1-(1-(1-d2)**r)**b)

while((p1temp < p1) | (p2temp > p2)):
    if((p2temp > p2) & (p1temp < p1)):
        r+=1
        p1temp = (1-(1-(1-d1)**r)**b)
        p2temp = (1-(1-(1-d2)**r)**b)
    elif (p1temp < p1):
        b+=1
    p1temp = (1-(1-(1-d1)**r)**b)
    p2temp = (1-(1-(1-d2)**r)**b)
    print ("P1: " + str(p1temp))
    print ("P2: " + str(p2temp))

print("r = " + str(r))
print("b = " + str(b))
print("p1 = " + str(p1temp))
print("p2 = " + str(p2temp))