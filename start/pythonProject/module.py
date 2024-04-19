# use module

import random  # can import all
import math
from random import shuffle, choice  # can import partially

data = [1, 2, 3, 4, 5, 6]
result = random.choice(data)
print(result)
random.shuffle(data)
print(data)

print(math.fabs(-10.123))
