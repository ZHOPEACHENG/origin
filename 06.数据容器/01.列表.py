list = [1, 2, 3, 4, 5]
B = list.index(1)
print(B)

list.insert(1, 6)
print(list)

list.append(7)
print(list)

list1 = [1,2,3]
list.extend(list1)
print(list)
list.append(list1)
print(list)

list.remove(1)
print(list)

del list1[1]
print(list1)

C = list1.pop(0)
print(list1)
print(C)

len(list1)

list1.extend([1,2,3])
list1.reverse()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

D = list1.count(3)
print(D)

new_list = list.copy()
print(new_list)

list.clear()
print(list) # 列表已经清空
