import math
x=int(input("enter first number:"))
y=int(input("enter secend number:"))
if x>y:
    s=y
else:
    s=x
s+=1
for i in range(1,s):
    if((x%i==0)and(y%i==0)):
        bmm=i
print(bmm)