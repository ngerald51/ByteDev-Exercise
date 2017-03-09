
def fibonacci(num):
    (a, b, sum) = (0, 1, 0)
    while a <= num - 1:
        print (a)
        if a % 2 == 0:
            sum += a
        (a, b) = (b, a + b)

    return sum

print (fibonacci(10))
