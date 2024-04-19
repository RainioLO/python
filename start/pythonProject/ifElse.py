day = "Sunday"
hungry = 0

if hungry == 1:
    if day == "Monday":
        print("Study")
    elif day == "Tuesday":
        print("sleep")
    elif day == "Sunday" or day == "Saturday":
        print("Yeah")
else:
    print ("What")

# breakpoint F8
count = 0
while count < 10:
    print('AAA')
    count += 1

count = 1
result = 0
while count <= 100:
    result += count
    count += 1
print(result)

count = 1
while (count <= 100):
    if (count % 2 == 1):
        print (count)
    count += 1

number = 5
result = 1
i = 1
# 1! -2! +3! -4!
while i <= number:
    result *= i
    i += 1

sum = 0
number = 1
while number <= 3:
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1
    if number % 2 == 0:
        sum -= result
    else:
        sum += result
    number += 1
print(sum)

# Range 2 - 100, // 1 or self (like 3, 5, 7, 11)

number = 2
while number <= 100:
    isPrime = True
    i = 2
    while i < number:
        if (number % i == 0): # No remainder for 17/i
            isPrime = False
            break
        i += 1
    if isPrime:
        print(number)
    number += 1













