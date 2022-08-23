import collections as c
import os
data = c.OrderedDict()
data[1] = "Emmanuel"
data[2] = "Josephine"
data[3] = "Tom"
data[5] = "Chris"
data[6] = "Sarah"
data2 = c.defaultdict()
data2[3] = "Jamie"
data2[1] = "Lulu"
data2[5] = 309
count = c.Counter
txt = "hdudwi203nqdndouuhjiknbzafmnbvcxq1234r54wasdxg76g4590532"
c1 = count(txt)
b = (c1.most_common())
#print(f"Your most common words are {b} ")
a = input("Enter any text to get the least word or number used: ")
a1 = count(a)
a2 = a1.most_common()
print(a2[-1])
print(os.path.basename(__file__))