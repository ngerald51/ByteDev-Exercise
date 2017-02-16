def fizz_buzz(x):
    i = 0
    while (i < x):
        i = i + 1
        if (i % 5 == 0) & (i % 3 == 0):
            print("FizzBuzz")
        elif ((i % 3) <= 0):
            print("Fizz")
        elif ((i % 5) <= 0):
            print("Buzz")
        else:
            print(i)


pass

fizz_buzz(5)