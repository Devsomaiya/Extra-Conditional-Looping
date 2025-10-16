###  Part E: Real-World If-Else + Loops (10 tasks)
# 43. Ticket price calculation with age-based discount.


TicketPrice=200
Age=int(input("Enter Age of the Person : "))


if Age <= 0:
    print("Invalid age entered!")
else:
    if Age<=3:
        Discount=100

    elif Age>3 and Age<=8:
        Discount=60

    elif Age>8 and Age<=12:
        Discount=30

    elif Age>12 and Age<18:
        Discount=15

    elif Age>=18 and Age<=60 :
        Discount=0

    elif Age>60:
        Discount=30

    print(f"Ticket Price = {TicketPrice} ")
    print(f"Applicable Discount: {Discount}%")
    TicketPrice=TicketPrice-( (TicketPrice*Discount)/ 100)
    print(f"Final Ticket Price = {TicketPrice} ")
