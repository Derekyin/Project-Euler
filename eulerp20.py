import math

fac = math.factorial(100)

list = list()
sum = 0
strfac = str(fac)
for i in range (0, len(strfac)):
    list.append(strfac[i])
print(list)

for i in range(0, len(list)):
    sum = sum + int(list[i])
print(sum)