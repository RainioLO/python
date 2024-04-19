# not duplicate
data = {245, 7, 27, 136, 8, -1, -1}
print(type(data))
print(data) # position change all the time

print(len(data))
data.add(9)
print(data)
data.remove(9)

print(178 in data)
data2 = {245, 7, 27, 8, -1}

print(data.intersection(data2)) # intersection
print(data.union(data2))
print(data.difference(data2)) # one data has, other not


