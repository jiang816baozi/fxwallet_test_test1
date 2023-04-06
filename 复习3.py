def grade_converter(grade):
    if grade>=90 :
        return " 优秀"
    elif 89<grade>80:
        return "良好"
    elif 79<grade<70:
        return "尚可"
    elif 69<grade<60:
        return"待改进"
    elif grade<60:
        return "不及格"

print(grade_converter(90))



#任务二
def using_control_once():
    if  1>0 :
        return"Success #1"
def using_control_again():
    if 1>0 :
        return "Sunccess #2"
print (using_control_again())
print(using_control_once())
