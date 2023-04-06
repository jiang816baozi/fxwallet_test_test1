def shut_down(s):
    if s == "yes" :
        return "关闭执行中"
    elif s== "no" :
        return "已取消关闭操作"
    else:
        return"对不起，无法执行"
print(shut_down("yes"))
print(shut_down("no"))
print(shut_down(999))




import math
def distance_from_zero(n):
    if type(n)==int or type(n)==float :
        return math.fabs(n)
    else:
         return "算不了"

print(distance_from_zero("你好"))



import math
print(math.sqrt(13689))



from math import sqrt
print(sqrt(13689))


def hotel_cost(nights):
    total =nights*488
    if type(nights)==int:
       return total

print(hotel_cost(3))

def train_cost(city):
    if city =="上海" :
        return 92.5
    elif city =="南京":
        return 117.5
    elif city == "苏州":
        return 111.5
    elif city == "西安":
        return 653.5
