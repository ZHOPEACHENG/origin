# 规则1：内容限定，只能使用：中文、英文、数字、下划线。注意:不能以数字开头
# 错误代码示范：
# 1_name = "Kaito"
# name_! = "Kaito"

#规则2：大小写敏感
name = "Kaito"
Name = "kaito"
print(name)
print(Name)

#规则3：不可以使用关键字
# 错误1：class = 11281222
# 错误2：def = 11281222
Class = 11281222