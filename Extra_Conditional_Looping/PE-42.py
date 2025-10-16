###  Part E: Real-World If-Else + Loops (10 tasks)
# 42. Menu-driven program: Calculator (+, -, *, /).

Exit=False
while not Exit:
    print("-------------SIMPLE CALCULATOR-------------")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Modulo ")
    print("6. Exit")

    operation=input("Enter the Operation You Want to Perform (1 or 2 or 3 or 4 or 5 or 6)  : ")
    if operation=="6":
        print("Exiting Calculator...!")
        break

    num1=float(input("Enter First number : "))
    num2=float(input("Enter Second number : "))
    
    if operation=="1":
        Result=num1+num2 
        print(f"{num1} + {num2} = {Result} ")

    elif operation=="2":
        Result=num1-num2
        print(f"{num1} - {num2} = {Result} ")

    elif operation=="3":
        Result=num1*num2
        print(f"{num1} * {num2} = {Result} ")

    elif operation=="4":
        if num2==0:
            print("Division by 0 ERROR !! Exiting Calculator . . . .")
            break
        else:
            Result=num1/num2
            print(f"{num1} / {num2} = {Result} ")

    elif operation=="5":
        Result=num1%num2
        print(f"{num1} % {num2} = {Result} ")
        
    else :
        print("Invalid Operation !!!")
        break
    

    continueProcess=int(input("To Exit press 0 and to continue press 1 : "))
    if continueProcess==1:
        Exit=False
    elif continueProcess==0:
        Exit=True
    else:
        print("Invalid input ! Exiting . . . ")
        break
