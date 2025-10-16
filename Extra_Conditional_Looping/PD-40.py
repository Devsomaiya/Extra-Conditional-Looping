###  Part D: Looping Problems (10 tasks)
# 40. Generate a half pyramid with numbers.

"""
 1  
 2   2  
 3   3   3  
 4   4   4   4  
 5   5   5   5   5 

 """

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f" {i} ",end=" ")
#     print()

# ---------------------------------------------


"""
 1  
 1   2  
 1   2   3  
 1   2   3   4  
 1   2   3   4   5

"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f" {j} ",end=" ")
#     print()

# ---------------------------------------------


"""
                     1  
                 2   2  
             3   3   3  
         4   4   4   4  
     5   5   5   5   5

"""

# for i in range(1,6):
#     for k in range(1,6-i+1):
#         print("   ",end=" ")
#     for j in range(1,i+1):
#         print(f" {i} ",end=" ")
#     print()

# ---------------------------------------------


"""
                     1  
                 1   2  
             1   2   3  
         1   2   3   4  
     1   2   3   4   5

"""

for i in range(1,6):
    for k in range(1,6-i+1):
        print("   ",end=" ")
    for j in range(1,i+1):
        print(f" {j} ",end=" ")
    print()
