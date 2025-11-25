# 前置知识

# print语句不换行
print("Hello")
print("world")
print("Hello",end=' ')
print("world",end='')
# 制表符\t，使多行对齐
print("Hello world")
print("Love ACHENG")
print("Hello\tworld")
print("Love\tACHENG")


# 九九乘法表
y = 1
while y < 10:

    x = 1
    while x <= y:
        print(f"{x} * {y} = {x * y}\t", end='')
        x += 1

    y += 1
    print()     # print空内容，输出一个换行


