word=input("Enter the word : ")

countVo=0
countCon=0
for i in word:
    if i=='a' or i=='A' or  i=='e' or i=='E' or  i=='i' or i=='I' or  i=='o' or i=='O'  or i=='u' or i=='U':
        countVo+=1
    else:
        countCon+=1
print(f"Vowels = {countVo} Consonants={countCon}")
