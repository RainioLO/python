
# 全局
a = 11
b = 21


def testfunc():
    a = 10
    b = 20
    return a, b


c, d = testfunc()
print(a, b, c, d)  # 11 21 10 20


