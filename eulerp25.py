

fibo = [1, 1]
i = 0

while len(str(fibo[i])) < 1000:
    fibo.append(fibo[-1]+fibo[-2])
    #print("The index of %s is %s " % (fibo[i]), i +2)
    i+=1
print("the first fib sequence with over 1k digit is %s " % (i+1))