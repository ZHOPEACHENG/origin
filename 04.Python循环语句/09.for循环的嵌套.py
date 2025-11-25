i = 0  # 提前定义i变量，如果不定义，i作为临时变量在规范上是作用于循环内部的，将导致第10行代码不规范
for i in range(1, 101):
    print(f"今天是向阿橙表白的第{i}天")

    for j in range(1, 11):
        print(f"给阿橙送的第{j}朵玫瑰花")

    print("阿橙我喜欢你！")

print(f"第{i}天表白成功")

# for循环和while循环可以相互嵌套