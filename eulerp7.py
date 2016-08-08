a = 0
num = 1


def checkPrime(num ):
    for i in range(0, num):
        if num % i ==0:
            num += 1
            return False
        else:

            return True

while True:
    checkPrime(num)

