###  Part D: Looping Problems (10 tasks)
# 32. Find the GCD (HCF) of two numbers using loops.

n1=int(input("Enter a number : "))
n2=int(input("Enter a number : "))

if n1<=n2:
    limit=n1
else:
    limit=n2
    
GCD=1
for i in range(1,limit+1):
    if n1%i==0 and n2%i==0 and i>=GCD:
        GCD=i 
print(f"GCD for {n1} and {n2} = {GCD}")
    
