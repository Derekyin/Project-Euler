sum = 0
x = 999999
times = 0
currentnum =0
max = times

def checkmax(a):
    global max
    if a > max:
        max = a
    return max

def recursive_collatz(n):
    global currentnum
    global times
    if n == 1:
        print("%s collatz %s times, current max: %s, number causing max %s" % (x, times,checkmax(times), currentnum))
        times = 0
        #checkmax(times)

        return n
    else:
        if n % 2 == 0:
            if times==0:
                currentnum = n
            times = times +1
            return recursive_collatz(n/2)
        if n % 2 != 0:
            if times==0:
                currentnum = n
            times = times + 1
            return recursive_collatz(3*n +1)


while x > 1:
    recursive_collatz(x)
    x = x -1