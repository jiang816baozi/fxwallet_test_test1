"""
1.要求用户输入一个英文单词
2.检查用户输入的值是否是一个英文单词
3.把这个英文单词翻译成Pig Latin（注意大小写变换）
4.把翻译结果线上在屏幕上
"""
original= input("请输入一个英文单词：")
the_string= original.lower()
a=the_string[0]
name="ay"
name_1= name + a
name_2 =the_string[1:len(original)] + name_1






if len(original)>0 and original.isalpha()==True:
    print(name_2)
else:
    print("输入单词不合法")


