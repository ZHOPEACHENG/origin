while True:
    import random
    num = random.randint(1,100)
    guess_num = int(input("输入猜测数字："))
    times = 1
    while guess_num != num:
        times += 1
        if guess_num > num:
            print("大了")
        else:
            print("小了")
        guess_num = int(input("再次输入："))
    print(f"猜了{times}次")



