#普通的if语句
if 10>15:
    print ("success")
#增加elif 意思是多个if条件一起判断
elif 6>12 :
    print ("succcess 1")
else:#代表是如果前面两个条件都不成立的话则返回这个结果
    print("fake")

#response = 'Y'

answer = "Left"
if answer == "Left": #if和变量一起判断
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")

# 在函数中加入条件语句
def using_control_once():
    if 1>0:
        return "success #1"
    elif 2<1:
        return "success #2"

print(using_control_once())

#函数、变量还有if条件语句、elif、一起
def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:
        return -1
    else:
        return 0
print (greater_less_equal_5(10))

#之前判断条件全部用在if中
def the_flying_circus():
    # Start coding here!
    if 13< 2 and not False:
        return True
    elif 1 == 1 and 1 != 2 and 1 < 2 and 1 <= 2 and 1 > 2 or 1 >= 2:
        return True
    else:
        return False
print(the_flying_circus())