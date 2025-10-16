###  Part C: Nested If-Else (10 tasks)
# 26. Print whether a given date (dd, mm, yyyy) is valid or not.


day=int (input ( "Enter the day : "))
month=int (input ("Enter the month : "))
year=int (input ("Enter the year : "))



if year>0 and day>0 and month>0:
    # if day<=31 and month<=12 and year<=2025:
    if ( month==1 or  month==3 or  month==5 or  month==7 or  month==8 or  month==10 or  month==12 ) and day<=31:
        print("The date is Valid")
    
    elif ( month==4 or  month==6 or  month==9 or  month==11 ) and day<=30:
        print("The date is Valid")
    
    elif month==2 :
        
        if ( (year%4==0 and year%100 !=0) or year%400==0) :
            if day<=29:
                print("The date is valid")
            else:
                print("The date is Not valid")

        else:
            if day<=28:
                print("The date is valid")
            else:
                print("The date is Not valid")

    else:
        print("The date is Not valid")
else:
    print("The date is Not valid")

    