
###  Part B: If-Else with Loops (10 tasks)

# 13. Find the factorial of a number using a loop.


num=int(input("Enter a number : "))

fact=1
i=1
while i<=num:
    fact*=i
    i+=1

print(f"Factorial Of the Number {num} is  = {fact} ")
