name = "Kaito"          # %表示我要占位
message = "%s学IT"%name # s表示将变量变成字符串放入占位的地方
print(message)


# 通过占位的形式，完成数字与字符串的拼接
age = 18
word = "我是：%s,我的年龄是：%s岁"%(name,age)
print(word)

# 类似的，%d和%f分别表示将变量变成整数和浮点数放入占位的地方
name_girl = "ACHENG"
name_boy = "AYAO"
birthday = 11281222
anniversary = 6.22
message = "我是%s，%s是我家的小猫，我们的生日是%d，%f是我们的纪念日"%(name_boy,name_girl,birthday,anniversary)
print(message)


# 字符串的快速格式化
# f"内容{变量}"进行快速格式化
print(f"我是{name_boy}，{name_girl}是我家的小猫，我们的生日是{birthday}，{anniversary}是我们的纪念日")