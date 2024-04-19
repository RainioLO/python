# 1000 phone number

list = []
print(type(list))
#        0      1     2
list = [1123, 2213, 34324]

print(list[0])
print(list[-3])

list[0] = "Pol"
print(list[0])
list.append('8787')
list.insert(1, '85698')
del list[0]
list.pop(0) # by index
list.remove(2213) # by value
print(list)

# Find min
data = [25,7,21,8,4,2,0,-23523,624,26]

min = 10000
index = 0
# length of the list len(data)

while index < len(data):
    if (data[index] < min):
        min = data[index]
    index += 1
print(min)

data1 = [1, 2, [3, 4, 5], 6, 'what']
print(data1)
print(data1[2][2])
print(len(data1[2]))

data2 = [[1,2,3,4], [5,-6,7,8], [9,10,11,-12]]
index = 0
max = 0
while index < len(data2):
    innerIndex = 0
    while innerIndex < len(data2[index]):
        if (data2[index][innerIndex] > max):
            max = data2[index][innerIndex]
        innerIndex += 1
    index += 1
print(max)

# Cut interface
data = [11, 42, 52, 74, 8568, 235, 48, 24646, 7757]
# 52, 74, 8568, 235, 48 2:7
# 52, 235 : 3
result = data[2:7:2]
print(result)
data.sort(reverse= True)
print(data)

result = 48 in data
print(result)

