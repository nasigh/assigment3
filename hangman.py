import random
Words = ['app' , 'python' , 'learn' , 'pc' , 'point' , 'number' , 'program' , 'snake']
Health = 5
Temp_array_True=[]
Word = random.choice(Words)
while True:
    Temp_Winner = 1
    for i in range (len(Word)):
        if Word[i] in Temp_array_True:
            print(Word[i],end=' ')
        else:
            print ('\U00002753',end=" ")
            Temp_Winner = 0
    if Temp_Winner == 1:
        print("\n" ,"\U0001F929"," You Win ","\U0001F929")
        break
    print("\nEnter A Character :","\U0001F914")
    User_Choice= input()
    if User_Choice in Word:
        Temp_array_True.append(User_Choice)
        print ("Correct ","\U00002705")
    else:
        print ("Wrong","\U0000274c")
        Health -= 1
    if Health == 0:
        print("You Lose","\U0001F927")
        break