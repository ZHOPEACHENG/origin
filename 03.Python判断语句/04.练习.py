num = int(input("我想的数字是："))


if int(input("请你猜猜我想的数字：")) == num:
    print("恭喜你，第一次就猜对了！")
elif int(input("不对哦，再猜一次：")) == num:
    print("恭喜你，猜对了！")
elif int(input("又猜错，再猜最后一次：")) == num:
    print("恭喜你，猜对了！")
else:
    print("Sorry，全部猜错啦，我想的是：10")