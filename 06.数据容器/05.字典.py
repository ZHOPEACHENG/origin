dict = {"Kaito":12,"ACHENG":11}
print(dict)
print(dict.keys()) #返回字典所有键
print(dict.values()) #返回字典所有的值
print(dict.items()) #返回一个元组列表，每个元组包含一个键值对
print(dict["Kaito"]) #通过键访问对应的值
dict["Kaito"] = 13 #修改字典中对应的值
print(dict)
del dict["Kaito"]
print(dict) #删除字典中对应的值
dict["Kaito"] = 12


#del dict["Kaito"] #删除不存在的键时，会报错

dict.pop("Kaito") #删除字典中对应的值，并返回该值
print(dict)

dict["Kaito"] = 12  #再次添加键值对
print(dict)
a = len(dict)
print(a) #返回字典的长度