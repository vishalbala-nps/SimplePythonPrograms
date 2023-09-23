#Prints the following pattern:
#x + x^2/2! - x^3/3! + x^4/4! -........x^n/n!

x = int(input("Enter x: "))
n = int(input("Enter n: "))
sign = "+"
ans = 0
for i in range(2,n+1):
    power = x**i
    fct = 1
    for i in range(1,i+1):
        fct *= i
    if sign == "+":
        ans += power/fct
        sign = "-"
    else:
        ans -= power/fct
        sign = "+"

ans += x 
print(ans)