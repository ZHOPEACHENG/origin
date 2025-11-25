# 比较运算符
# == 判断内容是否相等
# != 判断内容是否不相等
# >  判断左侧是否大于右侧
# <  判断左侧是否小于右侧
# >= 判断左侧是否大于等于右侧
# <= 判断左侧是否小于等于右侧

# 布尔类型只有两个字面量，一个True，一个False

# 定义变量储存布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量1的内容是：{bool_1},类型是{type(bool_1)}")
print(f"bool_2变量1的内容是：{bool_2},类型是{type(bool_2)}")

num_1 = 6
num_2 = 22
print(f"6 == 22的结果是：{num_1 == num_2}")
print(f"6 != 22的结果是：{num_1 != num_2}")
print(f"6  > 22的结果是：{num_1  > num_2}")
print(f"6  < 22的结果是：{num_1  < num_2}")