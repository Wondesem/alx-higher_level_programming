#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    las_digit = number %  10
else:
    las_digit = number % (-10)
print("Last digit of ", number, "is", las_digit, end=" ")
if las_digit > 5:
    print("and is greater than 5")
elif las_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
