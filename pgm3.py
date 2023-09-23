# Check whether the given number is a prime or composite or neither prime/composite


no = int(input("Enter a number: "))
if no == 1:
    print("Neither Prime nor composite")
else:
    comp = False
    for i in range(1,no+1):
        if no % i == 0:
            if i == no or i == 1:
                pass
            else:
                comp = True
                break
    if comp:
        print(no,"is a composite number")
    else:
        print(no,"is a prime number")