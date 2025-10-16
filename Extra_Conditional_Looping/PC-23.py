###  Part C: Nested If-Else (10 tasks)
# 23. Check whether a given number lies in a range [x, y].

RS=int(input("Enter the Starting Of the Range : "))
RE=int(input("Enter the Ending Of the Range : "))

if RS>RE:
    temp=RS
    RS=RE
    RE=temp

num=int(input(f"Enter a number You Want To check For The Range {RS}-{RE} : "))

if num>=RS :
    if num<=RE:
        print(f"The Number {num} is in the Range {RS}-{RE}")
    else:
        print(f"The Number {num} is not in the Range {RS}-{RE}")

else:
    print(f"The Number {num} is not in the Range {RS}-{RE}")
