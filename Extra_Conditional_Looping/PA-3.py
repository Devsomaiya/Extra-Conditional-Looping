###  Part A: Basic If-Else (10 tasks)

# 3. Check whether a given year is a leap year or not.

year=int(input("Enter the year : "))


if (year%4==0 and year%100 !=0) or year%400==0:
    print(f"The Year {year} is Leap year")
else :
    print(f"The Year {year} is Not Leap year")
