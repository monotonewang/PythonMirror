def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end="")
        a, b = b, a + b
        print()


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


fib(1000)
print("----------")
print(fact(10))
