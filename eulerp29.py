unsorted = list()
temp = 0

for a in range (2, 101):
    for b in range (2, 101):
        temp = a **b
        if temp not in unsorted:
            unsorted.append(a**b)
unsorted.sort()

print(len(unsorted))