###  Part E: Real-World If-Else + Loops (10 tasks)
# 44. Shopping discount calculator (10% if bill > 1000).



Bill=0
numberofitems=int(input("How Many Items Purchased ? : "))
items=1
while items<=numberofitems:
    item=int(input(f"Enter the price of item {items}: "))
    if item<0 :
        print("Invalid item Price Entered!")
    else:
        items+=1
        print()
        Bill+=item


if Bill<=100:
        Discount=0

elif Bill<=1000:
        Discount=5

else :            #Bill>1000
        Discount=10

print(f"Bill = {Bill} ")
print(f"Applicable Discount: {Discount}%")

Bill=Bill-( (Bill*Discount)/ 100)
print(f"Final Bill = {Bill} ")
