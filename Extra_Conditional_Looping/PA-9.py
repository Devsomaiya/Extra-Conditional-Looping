
###  Part A: Basic If-Else (10 tasks)
# 9. Check whether a character is uppercase, lowercase, digit, or special symbol


# character=input("Enter a character :")
# ch=character[0]


# if ch.islower():
#     print("Lower Case Letter")
# elif ch.isupper():
#     print("Upper Case Letter")
# elif ch.isnumeric():
#     print("Digit")
# else:
#     print("Special Symbol")
    


character=input("Enter a character :")
ch=character[0]

if ch=='a'or ch=='b'or ch=='c'or ch=='d'or ch=='e'or ch=='f'or ch=='g'or ch=='h'or ch=='i'or ch=='j'or ch=='k'or ch=='l'or ch=='m'or ch=='n'or ch=='o'or ch=='p'or ch=='q'or ch=='r'or ch=='s'or ch=='t'or ch=='u'or ch=='v'or ch=='w'or ch=='x'or ch=='y'or ch=='z':
    print("Lower Case Letter")
elif ch=='A'or ch=='B'or ch=='C'or ch=='D'or ch=='E'or ch=='F'or ch=='G'or ch=='H'or ch=='I'or ch=='J'or ch=='K'or ch=='L'or ch=='M'or ch=='N'or ch=='O'or ch=='P'or ch=='Q'or ch=='R'or ch=='S'or ch=='T'or ch=='U'or ch=='V'or ch=='W'or ch=='X'or ch=='Y'or ch=='Z':
    print("Upper Case Letter")
elif ch=='1' or ch=='2' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9' or ch=='0' :
    print("Digit")
else:
    print("Special Symbol")

