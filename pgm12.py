#Program to print the largest and second largest number in a given list
lst = []
nlist = []
while True:
    no = input("Enter a number. Press enter to Stop: ")
    if no == "":
        break
    else:
        lst.append(int(no))

max1 = lst[0]
for i in range(1,len(lst)):
    if lst[i] > max1:
        max1 = lst[i]

for i in lst:
    if i != max1:
        nlist.append(i)

max2 = nlist[0]
for i in range(1,len(nlist)):
    if nlist[i] > max2:
        max2 = nlist[i]
print(max1)
print(max2)