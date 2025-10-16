
###  Part B: If-Else with Loops (10 tasks)

# 19. Check whether a number is an Armstrong number (e.g., 153 → 1³+5³+3³ = 153).


num=int(input("Enter a number : "))
NUM=num

sum=0
NoOfDigits=0
while NUM/10>0:
    NoOfDigits+=1
    NUM=NUM//10

NUM=num
while NUM/10>0:
    sum=sum+(NUM%10)**NoOfDigits
    NUM=NUM//10 

if sum==num:
    print(f"{num} is an Armstrong number ")
else :
    print(f"{num} is Not an Armstrong number ")
 

