n= int(input("enter number:"))
i=0 
s=0
z=n 
y=n
while n!=0:
    n=n//10
    i+=1
print("tedad argham:",+i)
while z>0:
    b=z%10
    s+=b**i
    z//=10
if y==s:
    print("yes")
else:
    print("no")