###  Part B: If-Else with Loops (10 tasks)

# 16. Count how many digits are in a given number.



num=int(input("Enter a number : "))
NUM=num

No_Digits=0
while NUM/10>0:
    No_Digits+=1
    NUM=NUM//10


print(No_Digits)