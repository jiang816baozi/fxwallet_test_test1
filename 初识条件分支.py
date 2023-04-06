



def choice():
    print("请选择，左还是右：")
    answer =input("输入左或者右：")
    if answer =="左"or answer =="左边":
       print("你选择了左")
    elif answer == "右" or answer =="右边":
        print("你选择了右")
    else :
        print("你两个都没选，你决定再试一次")
        choice()

    choice()

