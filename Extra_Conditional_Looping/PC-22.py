###  Part C: Nested If-Else (10 tasks)
# 22. Find the largest of three numbers using nested if.
n1=int(input("Enter a number 1  :"))
n2=int(input("Enter a number 2  :"))
n3=int(input("Enter a number 3  :"))

if n1 == n2 == n3:
    print("All numbers are equal")
elif n1>n2:
    if n1>n3:
        print(f"{n1} is Largest number")
    else :
        print(f"{n3} is Largest number") 
else :
    if n2>n3:
        print(f"{n2} is Largest number")
    else :
        print(f"{n3} is Largest number")       

