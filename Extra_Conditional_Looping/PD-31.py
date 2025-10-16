###  Part D: Looping Problems (10 tasks)
# 31. Print Fibonacci series up to N terms.
FirstTerm=0
SecondTerm=1

N=int(input("Enter how many terms you want : "))
Nthterm=FirstTerm+SecondTerm
if N<=0:
    print("Enter valid number")
elif N==1:
    print(f"{FirstTerm}",end=" ")
elif N==2:
    print(f"{FirstTerm} {SecondTerm}",end=" ")
else:
    print(f"{FirstTerm} {SecondTerm}",end=" ")
    for i in range(1,N-1):
        FirstTerm=SecondTerm
        SecondTerm=Nthterm
        print(Nthterm,end=" ")
        Nthterm=FirstTerm+SecondTerm
