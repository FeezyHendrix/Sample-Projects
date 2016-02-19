def fibonacci(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
        yield a

amount = int(input('Enter the amount of fibonacci numbers to output:'))
for i in fibonacci(amount):
    print(i, end=' ')
