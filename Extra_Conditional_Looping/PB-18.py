###  Part B: If-Else with Loops (10 tasks)

# 18. Check whether a number is a palindrome (e.g., 121 → palindrome).


num=int(input("Enter a number : "))
NUM=num 

No_Digits=0
while NUM/10>0:
    No_Digits+=1
    NUM=NUM//10

numString=str(num)
count=0

for i in range(0,No_Digits//2):
    if numString[i]==numString[No_Digits-1-i]:
        count+=1
    


if count==No_Digits//2:
    print("Pelindrome")
else :
    print("Not Pelindrome")