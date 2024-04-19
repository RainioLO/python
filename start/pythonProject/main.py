print("hello")

'''
print("hello1")
print("hello2")
'''

# print("hello3")

# int, float, bool, str

print(type(123))  # get the type of the data
print(type(str(123)))

#         整除  次方
# + - * / // %  **   ()

print(type(2**3))
# 400, -50, use first and calculate, now $10000, with 200.3, how much ?

print(10000-(10000-200.3) // 400*50-200.3)

price = 10000
discount = 200.3
extractDiscount = (price-discount) // 400 * 50
result = price - discount - extractDiscount
print(result)

print(id(result)) # get the address



