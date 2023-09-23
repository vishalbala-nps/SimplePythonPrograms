#Program to input a list of numbers and check if it is an Armstrong number. If so, find the largest and smallest in the given list
lst = []
while True:
    no = input("Enter a number. Press enter to Stop: ")
    if no == "":
        break
    else:
        lst.append(int(no))

cublist = []
for i in lst:
    cubsum = 0
    for j in str(i):
        cubsum += int(j)**3
    if cubsum == i:
        cublist.append(i)
print("Maximum Armstrong number:",max(cublist))
print("Minimum Armstrong number:",min(cublist))