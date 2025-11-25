import random
num = random.randint(1,10)
print("请你猜一个1到10之间的数字，你有三次机会。")
guess_num1 = int(input("输入你判断的数字："))
if  guess_num1 == num:
    print("恭喜你，一次就猜对了！")
else:
    if guess_num1 > num:
        print("你猜的数字大了哦。")
    else:
        print("你猜的数字小了哦。")
    guess_num2 = int(input("请再猜一次："))
    if guess_num2 == num:
        print("恭喜你，猜对了！")
    else:
        if guess_num2 > num:
            print("你猜的数字大了哦。")
        else:
            print("你猜的数字小了哦。")
        guess_num3 = int(input("请最后猜一次："))
        if guess_num3 == num:
            print("恭喜你，猜对了！")
        else:
            print("很遗憾，你没有猜中哦。")
            print(f"正确答案是：{num}")