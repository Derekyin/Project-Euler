import math

x = 3
num = 0
list = list()
while True:
    for i in range (0, len(str(x))):
        num = num+ math.factorial(int(str(x)[i]))
       #print(x)
    if x == num:
        list.append(x)
        print("current sum: %s" % sum(list))
    x+=1
    num = 0

