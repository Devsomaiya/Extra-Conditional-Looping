###  Part A: Basic If-Else (10 tasks)

# 10. Check if three sides form a valid triangle.


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")
