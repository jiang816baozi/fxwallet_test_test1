import time #引入time模块
print(time.time()) #时间间隔是以秒为单位的浮点小数，函数time.time()用于获取当前时间戳
print(time.localtime(time.time())) #将浮点数传递给如localtime函数,返回浮点数的时间戳方式转换为时间元组
print (time.asctime(time.localtime(time.time())))# 使用函数asctime 将时间格式化比较好读的形式
today_date = (time.localtime(time.time()))
print(today_date)
