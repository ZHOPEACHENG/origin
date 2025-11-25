def add(x, y):
    result = x + y
    print(f"{x} + {y}的结果是{result}")

add(1, 2)



# 练习案例
def check(num):
    if num <= 37.5:
        print(f"您的体温是:{num}摄氏度，体温正常请进!")
    else:
        print(f"您的体温是:{num}摄氏度，需要隔离！")

check(float(input("请输入体温：")))