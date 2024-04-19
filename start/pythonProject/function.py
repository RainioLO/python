from typing import Tuple


def aaa():
    print('aaaa')


aaa()


# add type
def add(number1: int, number2: int = 5) -> tuple[int, int, int]:  # number2 default 5
    return number1 + number2, number1, number2  # return the turple


add(1, 2)
result = add(1)
print(result)


# 153 = 1*1*1 + 5*5*5 + 3*3*3 -> True

def is_iris(number: int) -> bool:
    sum = 0
    if number > 999 or number < 100:
        return False
    temp = number  # if no -> change the value of number directly
    while temp > 0:
        sum += ((temp % 10) ** 3)
        temp //= 10  # need to be 整除
    return sum == number


def is_iris2(number: int) -> bool:
    sum = 0
    if number > 999 or number < 100:
        return False
    number = str(number)
    sum = int(number[0]) ** 3 + int(number[1]) ** 3 + int(number[2]) ** 3 # remember to change the type
    return sum == int(number)

print(is_iris(153))
print(is_iris2(153))


