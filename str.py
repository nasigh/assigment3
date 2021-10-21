str=input("write your sentence:").strip()
i=0
space = False
for x in str:
    if x==" ":
        if space == False :
            i+=1
            space = True
    else:
        space = False
print(f"tedad: {i+1}")