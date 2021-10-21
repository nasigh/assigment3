import random
n = input ("please enter n:")
i=0
array=[]
while i< int(n):
 x = random.randint(1,100)
 if not  (x in array):  
  array.append (x)
 i=i+1
print(array)
