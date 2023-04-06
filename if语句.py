username ='admin'
password = '123'
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
	print('身份验证成功!')
else:
	print('身份验证失败!')

if 810< 9:
    print("I get printed!")
elif 80> 9:
    print("I don't get printed.")
else:
    print("I also don't get printed!")
"""
if 条件语句
格式如下
if 8<9
   print"xxxxx"
还有elif 就是多个if条件
else就是反之则xxx意
"""
