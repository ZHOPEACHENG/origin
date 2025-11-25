num = 500  # num为全局变量
def add1():
    global num2  # 将局部变量修改为全局变量，需写在函数声明之前
    num2 = num + num # num2为局部变量
    print(num2)

add1()
print(num2) #局部变量只能在函数内使用，若想在函数外使用，需要修改为全局变量

