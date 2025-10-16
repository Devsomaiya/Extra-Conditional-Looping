###  Part C: Nested If-Else (10 tasks)
# 25. Find if a character is alphabet and if so, vowel/consonant.
character=input("Enter A Character : ")
ch=character[0]


if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
    print("The Character is An Alphabet")
    if ch=='a' or ch=='A' or  ch=='e' or ch=='E' or  ch=='i' or ch=='I' or  ch=='o' or ch=='O' or  ch=='u' or ch=='U' :
        print("The Character is a Vowel")
    else :
        print("The Character is a Consonant")
else:
    print("The Character is Not An Alphabet")


