#Menu Driven program to check if a given string is a palindrome, or printing each word in a separate line and return the length
while True:
    opt = input("Menu:\n1. Check Palindrome\n2. Print each word in seperate line\n3. Exit\nEnter option: ")
    if opt == "1":
        txt = input("Enter a string: ")
        tlist = list(txt)
        ntlist = []
        for i in range(len(tlist)-1,-1,-1):
            ntlist.append(tlist[i])
        for i in range(0,len(ntlist)):
            if ntlist[i] != tlist[i]:
                print(txt,"is not a palindrome")
                break
        else:
            print(txt,"is a palindrome")
        break
    elif opt == "2":
        txt = input("Enter a string: ")
        tlist = txt.strip().replace("\t"," ").split(" ")
        words = 0
        for i in tlist:
            print(i)
            words += 1
        print("No of words in",txt,"is",words)
        break
    else:
        print("Invalid Input")
        continue
