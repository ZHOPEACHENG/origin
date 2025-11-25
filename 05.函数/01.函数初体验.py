# 函数是组织好的，可重复使用的，用来实现特定功能的代码段

name = "Kaito"
length = len(name)  #  len()是python的内置函数，用于统计长度
print(length)

# 统计字符串的长度，不适用len()函数
str1 = "Kaito"
str2 = "AYAO"
str3 = "ACHENG"

count = 0
for i in str1:
    count += 1
print(f"字符串str1的长度为{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串str2的长度为{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串str3的长度为{count}")
#  重复代码，效率低

#  定义函数，提高效率
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}")


my_len(str1)
my_len(str2)
my_len(str3)


