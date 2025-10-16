###  Part E: Real-World If-Else + Loops (10 tasks)
# 47. Print all unique elements from a list.



List=["cat","dog","Apple","cat","Apple","Bat","Rose"]

print(f"{List}")
print("All Unique Elements From the above List are : ")
for x in List:
    match=0
    for y in List:
        if x==y:
            match+=1
    if match==1:
        print(f"{x}")

    
        
        
        