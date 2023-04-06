#整数
int1 =1
int2 = 10
int3 = -5
#浮点数
float1 = 1.0
float2 = 10.
float3 = -5.5

pen =5
print("我想买"+str(pen)+"支签字笔")
price=4.25
total_cost = pen * price
print(total_cost)
if total_cost is int:
    print("整数")
else:
    print("浮点数")

