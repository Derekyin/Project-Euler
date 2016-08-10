total = list()
for i in range(1, 1001):

    total.append(i ** i)
    #print(i ** i)
sumstr = str(sum(total))
print(sumstr[len(sumstr)- 10 : len(sumstr)])