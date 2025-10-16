###  Part A: Basic If-Else (10 tasks)
# 6. Find the smallest of three numbers.

n1=int(input("Enter a num1 : "))
n2=int(input("Enter a num2 : "))
n3=int(input("Enter a num3 : "))


if n1<n2 and n1<n3:
    print(f"{n1} is smallest number ")
elif n2<n1 and n2<n3:
    print(f"{n2} is smallest number ")
else:
    print(f"{n3} is smallest number")