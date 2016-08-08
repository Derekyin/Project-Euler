sum = 2 ** 1000

sumstr = str(sum)
list = list()

totalSum =0
for i in range(0, len(sumstr)):
    list.append(sumstr[i])

print(list)

for i in range (0, len(list)):
    totalSum = totalSum + int(list[i])

print(totalSum)