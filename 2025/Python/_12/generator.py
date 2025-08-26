# Create a generator that outputs Fibonacci numbers
def genFib():
    a, b = 0, 1

    while True:
        yield b
        a, b = b, a + b

prime = []
genFib = genFib()

# Create a function that determines whether a number is prime
def primeNum(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# Create a list to store the first 4 Fibonacci numbers that are also prime
def fib4():
    while len(prime) < 4:
        fib = next(genFib)
        if primeNum(fib):
            prime.append(fib)


# Do this again (appending 4 more fib primes to your list) so you end up with 8 Fibonacci primes)
def fib8():
    while len(prime) < 8:
        fib = next(genFib)
        if primeNum(fib):
            prime.append(fib)


# Do it one last time but only get three fib primes the final time (This may be a bit slower since the numbers are so big)
def fib11():
    while len(prime) < 11:
        fib = next(genFib)
        if primeNum(fib):
            prime.append(fib)

fib4()
fib8()
fib11()

# Print the list to the console
print(prime)







