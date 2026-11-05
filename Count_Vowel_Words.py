Word = input("Enter A Word : ")
Count = 0

for i in Word:
    if i in "aeiou":
        Count += 1

print("Count Of Vowel Words : ", Count)