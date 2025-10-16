###  Part C: Nested If-Else (10 tasks)
# 29. Find whether a triangle is scalene, isosceles, or equilateral.


L1=int(input("Enter the Length of First Side : "))
L2=int(input("Enter the Length of Second Side : "))
L3=int(input("Enter the Length of Third Side : "))





if L1==L2==L3:
     print("The Triangle is equilateral")
elif L1==L2 or L2==L3 or L3==L1:
     print("The The Triangle is isosceles")
else:
     print("The Triangle is scalene")
