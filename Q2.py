
num1 = 1
num2 = 1
n = 0
res = 0
while n < 4000000:
    n = (num1 + num2)
    if n % 2 == 0:
        res = res + n
    num1 = num2
    num2 = n
print(res)    

