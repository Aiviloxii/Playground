# Write a python program that returns the multiples of four in a list.
prices = [32, 45, 100, 760, 50, 150, 80, 500, 25]
Fours = list(filter(lambda b: (b % 4 == 0), prices))
print(Fours)

