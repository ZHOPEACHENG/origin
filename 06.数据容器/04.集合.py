my_set = {1,2,3,4,5,1,2,3,3}
print(my_set)
my_set.add(6)   # 添加元素
print(my_set)
my_set.remove(4)  # 若元素不存在，则会报错
print(my_set)
my_set.discard(9)  # 功能同remove，若元素不存在，则不报错
print(my_set)
my_set.pop()  # 随机删除一个元素
print(my_set)
my_set.clear()  # 清空集合
print(my_set)
my_set = {1,2,3,4,5,1,2,3,3,9}
my_set.update({1,2,3,4,5,7})  # 合并两个集合
print(my_set)
my_set.difference_update({1,2,3,4,5})  # 集合差集
print(my_set)
my_set.intersection_update([1,2,3,4,5])  # 集合交集
print(my_set)
my_set.union([1,2,3,4,5,87])
print(my_set)
my_set.symmetric_difference_update([1,2,3,4,5])  # 集合对称差集
print(my_set)



