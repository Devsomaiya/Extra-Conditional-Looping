###  Part D: Looping Problems (10 tasks)
# 36. Print the sum of digits of a number.

num=int(input("Enter a number  : "))
NUMBER=num
sum=0
while num/10>0:
    NUM=num%10
    sum+=NUM
    num=num//10


print(f"The sum of digits of the {NUMBER} is {sum} ")
