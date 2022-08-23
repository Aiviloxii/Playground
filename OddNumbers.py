# Write a python code that prints odd numbers from a list.
marks = [2, 3, 4, 17, 28, 98, 33, 21, 5, 22, 21, 10, 15, 23]
odd = 0
while odd < len(marks):
    if marks[odd] % 2 != 0:
       print(marks[odd])
    odd = odd + 1
# print(len(marks ))