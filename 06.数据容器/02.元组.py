tuple = (1,2,3,[4,5,6]) #不可以修改元组中的元素，但可以修改元组中的列表元素
print(tuple)


A = tuple.count(1)
print(A)
B = tuple.index(2)
print(B)
C = len(tuple)
print(C)
tuple[3][0] = 100
print(tuple)


