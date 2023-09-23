#Menu Driven program to check if a number is either an armstrong number or a perfect number
while True:
    opt = int(input("Menu:\n1.Armstrong number\n2.Perfect number\nEnter option: "))
    if opt == 1:
        no = int(input("Enter a number: "))
        cubsum = 0
        for i in str(no):
            cubsum += int(i)**3
        if cubsum == no:
            print(no,"is an armstrong number")
        else:
            print(no,"is not an armstrong number")
        break
    elif opt == 2:
        no = int(input("Enter a number: "))
        sum=0
        for i in range(1,no+1):
            if no % i == 0 and i != no:
                sum += i
        if sum == no:
            print(no,"is a perfect number")
        else:
            print(no,"is not a perfect number")
        break
    else:
        print("Invalid option")
        continue