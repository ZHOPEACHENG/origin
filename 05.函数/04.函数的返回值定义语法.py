def add(x, y):
    return x + y
    # 返回值即返回给调用者的结果，就是可接收的函数结果

num = add(1,2)
print(num)

def add(x, y):
    return 0
    print(add(x,y))
    # 返回值即返回给调用者的结果，就是可接收的函数结果
    # return之后的代码不包含在函数内，不会执行

num = add(1,2)
print(num)