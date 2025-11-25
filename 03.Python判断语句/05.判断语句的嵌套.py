# 04.案例简化
# 如果满足第一个条件，无需继续输入数据。

if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于120cm，可以免费。")
else:
    print("身高大于120，不能免费哦")
    print("不过如果你的VIP等级大于3，可以免费")
    vip_lever = int(input("请输入你的VIP等级（1-5）："))
    var = 1 <= vip_lever <= 5
    if var and vip_lever > 3:
        print("vip等级大于3，可以免费。")
    elif not var:
        print("请正确输入数据！")
    else:
        print("不好意思，条件不满足，需要买票。")