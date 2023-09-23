#Program to print the number of vowels, spaces and consonants in a given string
txt = input("Enter a string: ")
vowel = space = cons = 0
for i in txt:
    if i in "aeiouAEIOU":
        vowel += 1
    elif i.isalpha():
        cons += 1
    elif i.isspace():
        space += 1
print(vowel)
print(space)
print(cons)