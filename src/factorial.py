def factorial(num):
    num1 = 1
    while num >= 1:
        num1 = num1 * num
        num = num - 1
    return num1

print (factorial(5))