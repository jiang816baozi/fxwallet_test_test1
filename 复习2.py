my_word = "python is hard"
print (len(my_word))
print(my_word.upper())#大写
#python字符串内建函数
print(my_word[:3])#0到3，不算3
print(my_word[:])#全部
print(my_word[1:8])#1到8，不算8
print(my_word[1],my_word[1:8])

x=1
print(f'{x+1}')#f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去