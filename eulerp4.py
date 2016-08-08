a = 999
b = 999


def checkPali(value):
    valueStr = str(value)
    if valueStr[::-1]==str(value):
        print(valueStr)
        return True
    else:
        return False


for a in range(999, 100, -1):
    for b in range (999, 100, -1):
        value = a * b
        checkPali(value)

