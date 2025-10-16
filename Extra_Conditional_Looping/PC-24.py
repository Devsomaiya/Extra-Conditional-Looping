###  Part C: Nested If-Else (10 tasks)
# 24. Check whether a year is a century leap year.

year=int(input("Enter the year : "))

if year%100==0:
    print(f"The year {year} is Century year ")
    if year%400==0:
        print(f"The Year {year} is a Century Leap year")
    else:
        print(f"The Year {year} is not a Century Leap year , it is only Century Year")   
else:
    print(f"The Year {year} is not a Century Leap year and {year} is not even a Century Year")
