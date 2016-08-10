sums = 0
amica = 0
#global amica
totalamica = list()

def factorsum(i):
    global sums
    global amica
    global totalamica

    sums = 0
    #print("factors of %s are " % (i), end='')
    for j in range(1, i):
        if i % j == 0:
            sums+= j
     #       print(" %s," % j , end='')
    #print("sum: %s " % sums)
    return sums


for k in range(0, 10001):
    if k == factorsum(factorsum(k)) and sums < 10000 and sums != 0:
        amica = sums + k
        if amica not in totalamica:
            totalamica.append(amica)
        print("amicable numbers are %s and %s, sum is %s, total is %s" % (k, sums, amica, sum(totalamica)))



