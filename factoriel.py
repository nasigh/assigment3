import math
num=int(input("enter number:"))
for x in range(num):
    r=math.factorial(x)
    if r > num:
        print("no")
        break
    elif r == num:
        print("yes")
        break