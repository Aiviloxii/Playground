# Your manager wants to increase the cost of items in the store by 30%.
# Write a python program to display the new price from a list containing the old prices.

prices = [2500, 1040, 500, 250, 300, 650, 900, 100]
d = 30/100
add_up = list(map(lambda b: ((b * d) + b), prices))
print(add_up)