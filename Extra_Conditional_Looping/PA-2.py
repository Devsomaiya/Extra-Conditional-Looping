###  Part A: Basic If-Else (10 tasks)
# 2. Find the largest of two numbers.

num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))


if num1>num2 :
    print(f"{num1} is bigger number")
elif num2>num1:
    print(f"{num2} is bigger number")

else:
    print("Both are equal")