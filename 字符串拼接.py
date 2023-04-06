#Python2和3通用的拼接方法
print("Good" + "good" + "study!")
#python3 推荐的拼接方法
print("{} {} {}!". format("Good","good","study"))
print("{2} {1} {0}!". format("Good","good","study"))
print("{}{:.3f}{}".format("我每顿吃",2.234567,"个包子"))#如果想保留x位小数，可以用{:.Xf},X代表多少位要保留
