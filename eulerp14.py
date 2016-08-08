sum = 0


def recursive_collatz(n):
    if n == 1:

        return n

    else:
        if n % 2 == 0:

            print(n)
            return recursive_collatz(n/2)

        if n % 2 != 0:
            print(n)
            #sum = sum + 1
            return recursive_collatz(3*n +1)

#while True:
recursive_collatz(13)