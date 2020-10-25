from math import sqrt
X=[185,170,168,179,182,188,180,180,183,180,180,177]
Y=[72,56,60,68,72,77,71,70,84,88,67,66]
c1x=X[0]
c1y=Y[0]
c2x=X[1]
c2y=Y[1]
c1=[]
c2=[]
c1.append(1)
c2.append(2)
for k in range(2,12):
    k1=sqrt((X[k]-c1x)**2 +(Y[k]-c1y)**2)
    k2=sqrt((X[k]-c2x)**2 +(Y[k]-c2y)**2)
    if k1<k2:
        c1x=(c1x + X[k])/2 
        c1y=(c1y + Y[k])/2
        c1.append(k+1)
    else:
         c1x=(c2x + X[k])/2 
         c2y=(c2y + Y[k])/2
         c2.append(k+1)
print(c1)
print(c2)
x=int(input("Enter the height: "))
y=int(input("Enter the weight: "))
k1=sqrt((X[k]-c1x)**2 +(Y[k]-c1y)**2)
fk2=sqrt((X[k]-c2x)**2 +(Y[k]-c2y)**2)
if k1<k2:
        c1x=(c1x + X[k])/2 
        c1y=(c1y + Y[k])/2
        print("Belongs to first Cluster")
else:
         c1x=(c2x + X[k])/2 
         c2y=(c2y + Y[k])/2
         print("Belongs to second cluster")
   
