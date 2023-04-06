skill_completed = "python Syntax"
case_study =13
points_per_case =5
points_total = 100+case_study*points_per_case
print("I got",str(points_total),"points!")
'''
python的学习使用中遇到了这个错误：can only concatenate str (not "int") to str；
上网查过后发现是因为我没有做数据类型的转换，python并不能像java一样，在做拼接的时候自动把类型转换为string类型;
故而需要进行一个类型转换，譬如将print(1+"a")改为print(str(1)+"a")就可以了；
'''

time_1 = 6
time_2 =0.5*3
time_3 =6*2
time_4 = time_1 +time_2 +time_3
print(time_4)
time_5= time_4+ 32
print(time_5)
