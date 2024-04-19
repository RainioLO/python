
# cannot be changed address unchange

data = (112, 6, [1,2,3,4,5], 264,34,63,2522)
print(type(data))
print(len(data))
print(6 in data)
print(data[2])

data[2][3] = 6
print(id(data[0]))
print(data)




