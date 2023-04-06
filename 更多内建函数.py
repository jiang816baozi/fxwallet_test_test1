#python 中有些方法是不用导入直接用的，也就是Python的内建方法（built in）
#之前有一些已经学过的 内建方法比如：upper（） lower（） str（）
game = "I like Wangzhe"
print(game)
print(len(game))#len()用来计算字符串的长度
print(game.lower())#转化为小写
print(game.upper())#大写
pi=3.14
print(str(pi))

#将字符串的第一次字符转换为大写
print("money".capitalize())
print("money".center(40,'#' ))


def biggest_number(*args):#带星号的参数名表示传入值是一个元祖，也就是说这个方法可以接受任意数量的数字
    print(max(args))#接收任意数量的数字，返回其中的最大值
    return max(args)

def smallest_number(*args):
    print(min(args))#接收任意数量的数字，返回其中最小值
    return min(args)
def distance_from_zero(arg):
    print(abs(arg))#接收一个数字，返回其绝对值
    return abs(arg)
biggest_number(-10,-5,5,10)
smallest_number(-10,-5,5,10)
distance_from_zero(-10)
print(type(biggest_number(-10,-5,5,10)))

print(type(42))
print(type(4.2))
print(type('面包'))
#type（）可以返回传入参数的数据类型

