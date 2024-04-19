data = [25, [233, 888], {1, 2, 3}, 'Hello', {'name': 'John', 'age': 16}]  # List

for d in data:  # d: for each
    print(d)

for d in data[2]:
    print(d)

for d in data[3]:
    print(d)

for d in data[4].items():  # item of each element in data[4] dict
    print(d)

for d in data[4].values():  # item of each element in data[4] dict
    print(d)

for d in range(1, 101, 2):  # 隔2 add
    print(d)

for d in enumerate(data): # with the index and the element in the data list
    print(d) # get the turple for us

# Turple (), Set {}, List [], Dict{Key:Value}

data = []
for number in range(1, 101):
    data.append(number)
print(data)

data2 = [number for number in range (1, 101)] # put the number to the List
print(data2)



