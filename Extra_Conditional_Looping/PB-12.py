###  Part B: If-Else with Loops (10 tasks)

# 12. Print the sum of first N natural numbers.

N=int(input("Enter a Number : "))

sum=0
for i in range(1,N+1):
    sum+=i

print(f"Sum of First {N} NAtural Numbers is = {sum}")
