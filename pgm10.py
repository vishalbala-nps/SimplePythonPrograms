#Program to input a list and shift all zeroes to right and put all non zero digits to the left
lst = []
nolist = []
zerolist = []
while True:
    no = input("Enter a number. Press enter to Stop: ")
    if no == "":
        break
    else:
        lst.append(int(no))

for i in lst:
    if i == 0:
        zerolist.append(0)
    else:
        nolist.append(i)
nolist.extend(zerolist)
print(lst)
print(nolist)