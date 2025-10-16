###  Part E: Real-World If-Else + Loops (10 tasks)
# 45. Count how many students passed/failed in a list.



marks=[]
noOfStudents=int(input("Enter the number of students : "))


for i in range(1,noOfStudents+1):
    MARKS=int(input(f"Enter the marks of Student {i} : "))
    marks.append(MARKS)

print()
i=1
noOfPassed=0
noOfFalied=0
for MARKS in marks:
    if MARKS>=40:
        noOfPassed+=1
        print(f"Student {i} Passed in the Exam.")

    else:
        noOfFalied+=1
        print(f"Student {i} Failed in the Exam.")
    i+=1

print()
print(f"Total Number of Students              :  {noOfStudents}")
print(f"Number of Students Who Passed Exam    :  {noOfPassed}")
print(f"Number of Students Who Failed Exam    :  {noOfFalied}")


