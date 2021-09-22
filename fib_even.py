def fibbonachi_even(count):
    fib = [0, 1]
    fib_even = []
    while len(fib_even) < count:
        if fib[0] % 2 == 0:
            fib_even.append(fib[0])
        c = fib[1]
        fib[1] = fib[0] + fib[1]
        fib[0] = c
    return fib_even

print(fibbonachi_even(4))