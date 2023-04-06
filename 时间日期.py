#学习Python标准库 datetime，用来处理时间日期
#首先我们要试用这个库需要先导入（import）它
from datetime import datetime #从 datetime 这个库import 了datetime 这个类
now = datetime.now()#用now（）这个方法取现在时间，并且保存在变量now里面
print(now)
print(now.year)
print(now.month)
print(now.day)
print("now.year=",format(2021))
print('{:02d}-{:02d}-{:4d}'.format(now.month,now.day,now.year))#:02d表示输出的数字需要保留两位整数，并且在只有一位数时候补0