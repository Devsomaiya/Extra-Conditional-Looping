###  Part D: Looping Problems (10 tasks)
# 33. Find the LCM of two numbers using loops.


n1=int(input("Enter a number : "))
n2=int(input("Enter a number : "))

LCM_Find=False
i=1

while LCM_Find==False: 
    N1=n1*i
    N2=n2*i

    if N1%n2==0 :
        LCM=N1
        LCM_Find=True
    elif N2%n1==0:
        LCM=N2
        LCM_Find=True
    i+=1
    

print(f"LCM for {n1} and {n2} = {LCM}")

# 15 25
# 30 50
# 45 75
# 60 100
# 75 