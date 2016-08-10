sums = 0
total = list()

for i in range(1, 9999999):

    for j in range (0, len(str(i))):
        sums += int(str(i)[j]) ** 5
   #vcxz print(" %s: %s " % (i, sums))
    if sums == i:
        total.append(i)
        print("fifth digit powers are %s , total atm: %s " %( i, sum(total)))
    sums = 0







