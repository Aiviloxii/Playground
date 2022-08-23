# Write a python code that returns the sum of even numbers from 10 to 200
number = 10
even = 0
while number <= 200:
    if number % 2 == 0:
        even = even + number
    number = number + 1
print(even)