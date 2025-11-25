salary = 10000
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{i},绩效分{num},低于5，不发工资，下一位")
        continue
    salary -= 1000
    print(f"向员工{i}发放工资1000元，账户余额还有{salary}元")
    if salary <= 0:
        break
print("工资发完了，下个月领取吧。")
###   代码存在问题：如果工资不是 1000的倍数，如 10500元，剩下 500元时，还会继续发1000元工资
###   所以需要先判断工资是否足够，再决定发不发工资
print()

salary = 10500
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{i},绩效分{num},低于5，不发工资，下一位")
        continue
    if salary >= 1000:
        salary -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还有{salary}元")
    else:
        print("工资发完了，下个月领取吧。")    ###  此处，如果进入if发完最后一个人，还剩500元，并不会立刻执行break
        break                             ###  而是继续进入下一个循环中，继续判断，直到判断进入else才会执行break


###  可优化
    """
        else:                                      >>>>   继续嵌套   if salary < 1000:
            print("工资发完了，下个月领取吧。")         >>>>                 print("工资发完了，下个月领取吧。")
            break                                  >>>>                 break
    """




###  几天后回顾的反思：实际上，将第一版的  if salary <= 0:改成  if salary <= 1000:就可以了