def cube(n):

    return n**3

def add_three(n):
    if n %3 ==0 :
        return cube(n)
    else:
        return False

x= add_three(10)
print(x)
