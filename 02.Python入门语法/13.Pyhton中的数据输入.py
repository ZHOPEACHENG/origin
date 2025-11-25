# input输入语句
# print("你是谁")
# name = input()
# print("我知道了，你是：%s" % name)
# 简化为
name = input("你是谁")
print("我知道了，你是：%s" % name)

# 输入数字类型
num = input("你的银行卡密码是：") # input默认接受类型是字符串
# 数据类型的转换
num = int(num)
print("你的银行卡密码的类型是：",type(num))
