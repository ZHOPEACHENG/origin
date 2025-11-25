#  通过 range(num) 构建一个从0开始，到num结束的数字序列，该序列不含num本身
#  如range(5)取得的数据是：[0,1,2,3,4]
for x in range(5):
    print(x)
#  range(num1,num2)表示构建一个从num1开始，到num2结束的数字序列(不含num2本身)
for x in range(5, 10):
    print(x)
#  range(num1,num2,step)表示构建一个从num1开始，到num2结束的数字序列(不含num2本身)，step为数字之间的步长
#  step默认为 1
#  如range(5,10,2)取得数据为[5,7,9]
for x in range(5, 10, 2):
    print(x)


#  练习案例
i = 0
for x in range(1, 622):

    if x % 2 == 0:
        i += 1
print(i)

