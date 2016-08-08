f = open('p022_names.txt', 'r')
b = f.read()
c= b.split(",")
d = list()

score = 0
sums = 0
totalscore =0

def wordValue(d):
    global score
    global totalscore
    global sums

    for i in range(0, len(d)):
        for j in range(0, len(d[i])):
            sums = sums + (ord(d[i][j]) - 64)
        totalscore = totalscore + sums * (i + 1)
        print("%s: %s, %s" % (sums, d[i], totalscore))
        sums = 0

for i in range (0, len(c)):
    d.append(c[i][1:-1])
    d.sort()
wordValue(d)
