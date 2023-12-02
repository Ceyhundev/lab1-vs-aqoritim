from math import *
e=0.01
x=float(input("x:"))
t=sin(x)
s=0
n=1
while fabs(t)>e:
    
    s=s+t
    n+=1
    t=((-1)**(n+1))*((sin(x)**n)/n)

print(s)
