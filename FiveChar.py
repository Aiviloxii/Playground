# Write a python program that returns words using that are below five characters in a sentence.
me = ["Jayjay", "Ed", "Kenny Labau", "Kendrick Lamar", "Bree", "Snoop", "Eminem", "Pink", "Jack"]
me2 = "Hello! I am Olivia and am taking a course at Greg & CO ICT Hub."
meList = me2.split(" ")
chk = list(filter(lambda v: len(v) < 5, meList))

print(chk)
