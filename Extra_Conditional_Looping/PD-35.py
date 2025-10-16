###  Part D: Looping Problems (10 tasks)
# 35. Check whether a number is prime.


num=int(input("Enter a number : "))

count=0
for i in range(1,num+1):
    if num%i==0:
       count+=1

if count==2:
    print(f"The number {num} is prime number")
else :
    print(f"The number {num} is not a prime number")
