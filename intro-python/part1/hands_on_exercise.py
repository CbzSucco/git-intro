"""Intro to Python - Part 1 - Hands-On Exercise."""


"""import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi))
print(pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print(i)
if i < 50:
    print("i value is less than 50")
elif i== 50:
    print("i is equal to 50")
else:
    print("i value is greater than 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == 'orange':
    print("Picked fruit is an orange")
elif picked_fruit == 'strawberry':
    print("Picked fruit is a strawberry")
else:
    print("Picked fruit is a banana")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiplication(num1, num2):
    result = num1 * num2
    return result


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", multiplication(12,96))

print("48 x 17 =", multiplication(47,17))

print("196523 x 87323 =", multiplication(196523,87323))"""

fruits = {"apples": 5, "pears": 2, "oranges": 9 }
for fruit in fruits:
    print(fruit)

list(fruits.items())
for fruit in fruits.items():
    print(fruit.item)
