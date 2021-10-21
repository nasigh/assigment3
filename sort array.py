print ('Enter Array Length :')
Length_array=int(input())
Array = []
print("Enter Numbers In Array :")
for i in range(Length_array):
  Numbers = int(input()) 
  Array.append(Numbers)
print(Array)
Sorted_array = sorted(Array)
Temp_Sort = 0
for i in range(len(Sorted_array)):
    if Sorted_array[i] == Array[i]:
        Temp_Sort = 0
    else:
        Temp_Sort += 1
        break
if Temp_Sort == 0:
    print("\nSorted")
elif Temp_Sort != 0:
    print("\nNot Sorted")