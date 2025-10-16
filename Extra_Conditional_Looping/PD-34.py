###  Part D: Looping Problems (10 tasks)
# 34. Print all prime numbers from 1 to 100.


# num=int(input("Enter a number : "))
num=100
for x in range(1,num+1):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1

    if count==2:
        print(f"{x} ",end=" ")

