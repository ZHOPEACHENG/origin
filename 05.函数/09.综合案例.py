money = 5000000
name = input("请输入您的姓名：")

def check_money():
    """
    查询余额
    """
    print(f"当前余额为：{money}元")

def save_money():
    in_money = int(input("请输入您的存款金额："))
    global money
    money = money + in_money
    print(f"已存款{in_money}元，当前余额为：{money}元")

def withdraw_money():
    out_money = int(input("请输入您的取款金额："))
    global money
    money = money - out_money
    print(f"已取款{out_money}元，当前余额为：{money}元")

def main():
    print(f'''尊敬的{name}先生，您好！请问您需要办理什么业务呢？
    查询余额 \t【输入1】
    存款 \t【输入2】
    取款 \t【输入3】
    退出 \t【输入4】''')
    global option
    option = int(input("请输入你的选择："))

main()

while True:

    if option == 1:
        check_money()
    elif option == 2:
        save_money()
    elif option == 3:
        withdraw_money()
    elif option == 4:
        print("感谢您的使用，祝您生活愉快！")
        break
    else:
        option = int(input("请你正确输入："))
        continue
    main()
