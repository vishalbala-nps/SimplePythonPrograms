"""
Menu Driven program to print 2 patterns
Pattern 1:
      *
   *  *  *
*  *  *  *  *
   *  *  *
      *
Pattern 2:
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
"""
while True:
    opt = int(input("Menu:\n1. Pattern 1\n2. Pattern 2\nEnter an option: "))
    if opt == 1:
        space = 2
        for i in range(1,6,2):
            print("  "*space,end="")
            print("* "*i,end="")
            space -= 1
            print()
        space = 1
        for i in range(3,0,-2):
            print("  "*space,end="")
            print("* "*i,end="")
            space += 1
            print()
        break
    elif opt == 2:
        space = 0
        for i in range(5,0,-1):
            print("   "*space,end="")
            for j in range(1,i+1):
                print(j," ",end="")
            print()
            space += 1
        break
    else:
        print("Invalid option")
        continue
