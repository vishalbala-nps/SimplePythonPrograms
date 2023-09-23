#Program to input a list of numbers and swap elements at even index with the odd index
lst = []
lswap = []
isodd = False
last = 0
while True:
    no = input("Enter a number. Press enter to Stop: ")
    if no == "":
        break
    else:
        lst.append(int(no))
print("Original list:",lst)

if len(lst) % 2 != 0:
    isodd = True
    last = lst[-1]
    del lst[-1]

for i in range(0,len(lst),2):
    lswap.append(lst[i+1])
    lswap.append(lst[i])
if isodd:
    lswap.append(last)
print("Swapped list:",lswap)