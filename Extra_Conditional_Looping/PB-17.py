

###  Part B: If-Else with Loops (10 tasks)

# 17. Reverse the digits of a number using a loop.

num=int(input("Enter a number : "))
NUM=num 
NUM_REV=0

No_Digits=0
while NUM/10>0:
    No_Digits+=1
    NUM_REV=NUM_REV*10+NUM%10
    NUM=NUM//10

print(f"{num} --> {NUM_REV}   Length = {No_Digits}")
