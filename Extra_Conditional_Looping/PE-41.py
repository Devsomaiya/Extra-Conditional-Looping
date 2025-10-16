###  Part E: Real-World If-Else + Loops (10 tasks)
# 41. ATM machine: check PIN and balance withdrawal.



Balance=25000
pin="1234"

ValidAttempts=3
Exit=False
while Exit==False and ValidAttempts>0:
    print("What do you want to do : ")
    print("1. Check Balance    :  (press 1)")
    print("2. Withdraw Money   :  (press 2)")
    print("3. Deposit Money    :  (press 3)")



    choice=int(input("Your Choice of Action : "))


    CheckPin=input("Enter the Pin : ")
    if CheckPin==pin:



        if    choice==1 :
            print(f"Balnace = {Balance} ")

        elif  choice==2 :
            Amount=int(input("Enter the amount : "))
            if Amount>Balance :
                print("No Sufficient Balance in Your Account for this action !!")
            elif Amount <= 0:
                print("Invalid amount entered!")
            else:
                Balance-=Amount
                print(f"{Amount} is Withdran from your account ")
                print(f"Balnace = {Balance} ")

        elif  choice==3 : 
            Amount=int(input("Enter the amount : "))
            if Amount <= 0:
                print("Invalid amount entered!")
            else:
                Balance+=Amount
                print(f"{Amount} is Deposited into your account ")
                print(f"Balnace = {Balance} ")
        else:
            print("Invalid menu choice! Please select 1, 2, or 3.")
        
        ValidAttempts=3




    else :
        print("Invalid Pin !!")
        ValidAttempts-=1
        print(f"You have {ValidAttempts} Attemps Remaining")
        if ValidAttempts == 0:
            print("Too many incorrect attempts! Your account is locked.")
            break


        
    
    continueProcess=int (input("Do you Want to Continue OR not : (for Y press 1 OR for N press 2) : "))
    if continueProcess==1:
        Exit=False 
    elif continueProcess==2:
        Exit=True
        print("Thank you for using our ATM. Goodbye!")

    else:
        print("Invalid input! Exiting...")
        break
    
          

