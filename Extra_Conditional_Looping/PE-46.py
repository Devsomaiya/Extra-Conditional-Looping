###  Part E: Real-World If-Else + Loops (10 tasks)
# 46. Count how many words, digits, and special characters in a string.

stringSentence=input("Enter a String : ")

noOfWords=0
noOfSpace=0
word = ''
wordList = []
maxWordLength=0
wordLength=0
noOfDigits=0
noOfSpecial=0
noOfAlpha=0
noOfVowels=0
noOfConsonants=0
for x in stringSentence:
    if not x.isspace():
        noOfSpace=0
        word+=x
        wordLength+=1

        if x.isdigit():
            noOfDigits+=1

        elif x.isalpha() :
            noOfAlpha+=1
            if x=="a" or x=="A" or x=="e" or x=="E" or x=="i" or x=="I" or x=="o" or x=="O" or x=="u" or x=="U":
                noOfVowels+=1
            else:
                noOfConsonants+=1

        else:
            noOfSpecial+=1


    # elif x.isspace() :
    else:
        noOfSpace+=1

        if noOfSpace==1:
            noOfWords+=1
            wordList.append(word)

            if wordLength>=maxWordLength:
                maxWordLength=wordLength
            word = ''
            wordLength=0




noOfWords+=1
wordList.append(word)

if wordLength>=maxWordLength:
    maxWordLength=wordLength
word = ''
wordLength=0


print(f"Words : {wordList}")
print(f"no of Words : {noOfWords}")
print(f"Max Word Length : {maxWordLength}")
print(f"No of Alphabets : {noOfAlpha}")
print(f"No of Vowels : {noOfVowels}")
print(f"No of Consonants : {noOfConsonants}")
print(f"No Of Digits : {noOfDigits}")
print(f"No of Special Characters : {noOfSpecial}")
        