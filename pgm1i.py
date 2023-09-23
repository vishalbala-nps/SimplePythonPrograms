#Prints the value of the series: 
# 1 - x + x^2 - x^3 + x^4 -........x^n

x = int(input("Enter x: "))
n = int(input("Enter n: "))
sign = "+"
total = 0
for i in range(0,n+1):
    powered = x**i
    if sign == "-":
        total -= powered
        sign = "+"
    else:
        total += powered
        sign = "-"
print(total)

add = 0
sub = 0
for i in range(0,n+1,2):
    powered = x**i
    add += powered

for i in range(1,n+1,2):
    powered = x**i
    sub += powered

tot = add - sub
print(tot)
