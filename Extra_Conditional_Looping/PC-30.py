###  Part C: Nested If-Else (10 tasks)
# 30. Find whether roots of quadratic equation are real, equal, or imaginary.

a=int(input("Enter the the term a from Quadratic Equaation (ax2+bx+c=0) : "))
b=int(input("Enter the the term b from Quadratic Equaation (ax2+bx+c=0) : "))
c=int(input("Enter the the term c from Quadratic Equaation (ax2+bx+c=0) : "))

D=(b**2)-(4*a*c)


if D>=0:
    if D==0:
        print("The roots are real and equal")
    else:
        print("The roots are real and distinct (unequal)")
else:
    print("The roots are imaginary (or complex)")

