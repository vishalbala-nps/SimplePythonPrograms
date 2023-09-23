#Program to print the number of lower case charecters, upper case charecters, digits and special charecters in a given string
txt = input("Enter a string: ")
lc,uc,digit,special = 0,0,0,0
for i in txt:
    if i.islower():
        lc += 1
    elif i.isupper():
        uc += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        pass
    else:
        special += 1

print("Lower: ",lc)
print("Upper: ",uc)
print("Digit: ",digit)
print("Special Charecters: ",special)