height = int(input("请输入你的身高（cm）："))
vip_lever = int(input("请输入你的VIP等级（1-5）："))
var = 1 <= vip_lever <= 5
if height < 120:
    print("身高小于120cm，可以免费。")
elif var and vip_lever > 3:
    print("vip等级大于3，可以免费。")
elif not var:
    print("请你正确输入数据！")
else:
    print("不好意思，条件不满足，需要买票。")













