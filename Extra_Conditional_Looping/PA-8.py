###  Part A: Basic If-Else (10 tasks)

# 8. Find whether a number is divisible by 5 and 11.

num=int(input("Enter a number : "))

if num%5==0 and num%11==0:
    print(f"{num} is Divisible by 5 and 11 both")
elif num%5==0 :
    print(f"{num} is Divisible by 5 only")
elif num%11==0 :
    print(f"{num} is Divisible by 11 only")
else :
    print(f"{num} is Not Divisible by 5 and {num} is not Divisible by 11 ")
