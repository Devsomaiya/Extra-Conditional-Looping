
###  Part D: Looping Problems (10 tasks)
# 38. Print a pattern of stars (triangle).

"""
          *   
        *   *   
      *   *   *   
    *   *   *   *   
  *   *   *   *   *

"""
for i in range(1,6):
    for j in range(1,6-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*  ",end=" ")
    print()
