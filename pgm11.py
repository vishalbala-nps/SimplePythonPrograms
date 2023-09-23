#Program to extract 2 slices from a list of nos from 1 to 20
#The first slice includes every other number between indexes from 5 to 15 and then, finds the sum
#The second slice includes every 4th element of the list and then, finds its average
nos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
s1 = nos[5:15:2]
s2 = nos[3::4]
sums1 = 0
avg = 0
for i in s1:
    sums1 += i
for i in s2:
    avg += i
avg = avg/len(s2)
print("Sum of first slice: ",sums1)
print(s2)
print("Average of the 4th elements of the list:",avg)