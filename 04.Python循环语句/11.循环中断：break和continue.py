# continue
for i in range(1, 6):
    print("ACHENG")
    for j in range(1, 6):
        print("LOVE")
        continue  # 表示不执行后面的语句（仅针对本循环），继续循环
        print("AYAO")
    print("VERY MUCH")


print()


# break
for i in range(1, 6):
    print("ACHENG")
    for j in range(1, 10000000000000000000000000000000000000000000):
        print("LOVE")
        break  # 直接结束本循环
        print("AYAO")
    print("VERY MUCH")

