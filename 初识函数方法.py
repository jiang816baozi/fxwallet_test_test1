

def dicount(original_price):
    """
    满80减20
    :param original_price:
    :return: 折后价
    """
    new_price=original_price *0.85
    print("选择直接打完折的价格为:{}".format(new_price))
    return new_price
a =dicount(10)
# print(a)

def square(n):
    """
    计算一个数字的平方
    :param n:
    :return: 这个数字的平方值
    """
    squared = n**2
    print("{}的平方是{}.".format(n,squared))
    return squared
my_number_squared =square(10) #变量名=方法名（参数表）

def method_1():
    return 5
    print("我")

a= method_1()
print(a)
