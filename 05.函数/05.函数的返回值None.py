# None是类型'NoneType'的字面量，用于表示：空的，无意义的
print(type(None))
# 函数无return语句时默认返回值为None，也可以主动return None
def add(x, y):
    result = x + y

num = add(1,2)
print(num)

# 在if语句中，None等同于False
def check(num):
    if num < 18:
        return None
    else:
        return "OK"

result = check(16)
if not result:
    print("未成年")

# None也可以定义一些无初始内容的变量
name = None
