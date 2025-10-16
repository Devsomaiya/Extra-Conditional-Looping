###  Part C: Nested If-Else (10 tasks)
# 21. Input marks and print grade (A, B, C, D, Fail).

marks=int(input("Enter Marks : "))

if marks>=90:
    print("Grade A")
elif marks>=75 and marks<90:
    print("Grade B")
elif marks>=60 and marks<75:
    print("Grade C")
elif marks>=40 and marks<60:
    print("Grade D")
else :
    print("Fail")
