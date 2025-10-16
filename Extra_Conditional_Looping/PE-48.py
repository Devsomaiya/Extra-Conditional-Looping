###  Part E: Real-World If-Else + Loops (10 tasks)


# 48. Find the second largest number in a list.

List=[34,12,45,2,87,25,78]

print(f"List                              : {List}")

length=0
for x in List:
    length+=1

LargestNumber=0
for i in range(0,length):
                  
    for j in range(0,length-1-i):

        if List[j]>List[j+1]:

            temp=List[j]
            List[j]=List[j+1]
            List[j+1]=temp


print(f"List Elments in Ascending Order   : {List}")

print(f"Second Largest Number in the List : {List[length-2]}")