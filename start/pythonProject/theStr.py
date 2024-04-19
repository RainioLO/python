data1= "sadasdfdsg55" # cannot be changed
data3 = """
11
12
13
"""

print(data3)
print(len(data1))
print(data1[:2]) # cut with [0:2:1]

result = data1.replace('s', 'oi') # add the temp value, repoint to other direction
print(data1)
print(result)

index = data1.find('sad')
print(index)
print(data1.split('sd'))

# 1.
# %d, %f, %s
# %d 整數
# %f 小數
# %s str
name = 'John'
age = 13

data = 'Hello, %s, are you %d years old?' % (name, age)
print(data)

# 2. format
data = 'Hello, {}, are you {} years old?'.format(name, age)
print(data)

# 3. f-string
data = f'Hello, {name}, are you {age} years old?'
print(data)

#1*1=1
#1*2=2   2*2=4
#1*3=3   2*3=6   3*3=9
#1*4=4   2*4=8   3*4=12  4*4=16
#1*5=5   2*5=10  3*5=15  4*5=20  5*5=25
#1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
#1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
#1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
#1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81

for i in range(1, 10):
    row = ""
    for j in range(1, i + 1):
        equation = f"{j}*{i}={i*j}"
        row += equation + "   "
    print("#" + row.strip())




