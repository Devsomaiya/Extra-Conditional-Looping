###  Part D: Looping Problems (10 tasks)
# 39. Print a square number pattern using loops.


""""
 1   1   1   1   1  
 2   2   2   2   2  
 3   3   3   3   3  
 4   4   4   4   4  
 5   5   5   5   5 

"""
# for i in range(1,6):
#     for j in range(1,6):
#         print(f" {i} ",end=" ")
#     print()




# -----------------------------------------------------
""""
 1   2   3   4   5  
 1   2   3   4   5  
 1   2   3   4   5  
 1   2   3   4   5  
 1   2   3   4   5  

"""
# for i in range(1,6):
#     for j in range(1,6):
#         print(f" {j} ",end=" ")
#     print()




# -----------------------------------------------------

""""
   1        2        3        4        5     
   6        7        8        9        10    
   11       12       13       14       15    
   16       17       18       19       20    
   21       22       23       24       25  

"""
# num=1
# for i in range(1,6):
#     for j in range(1,6):
#         if num<=9:
#             print(f"   {num}    ",end=" ")
#         else:
#             print(f"   {num}   ",end=" ")
#         num+=1
#     print()




# -----------------------------------------------------

""""
   0        2        3        4        5     
   6        0        8        9        10    
   11       12       0        14       15    
   16       17       18       0        20    
   21       22       23       24       0 

"""


# num=1
# for i in range(1,6):
#     for j in range(1,6):
#         if i==j :
#             print(f"   0    ",end=" ")
#         else:
#             if num<=9:
#                 print(f"   {num}    ",end=" ")
#             else:
#                 print(f"   {num}   ",end=" ")
#             num+=1
#     print()



# -----------------------------------------------------

""""
   0        0        0        0        0     
   0        1        2        3        0     
   0        4        5        6        0     
   0        7        8        9        0     
   0        0        0        0        0  

"""


num=1
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print(f"   0    ",end=" ")
        else:
            if num<=9:
                print(f"   {num}    ",end=" ")
            else:
                print(f"   {num}   ",end=" ")
            num+=1
    print()
