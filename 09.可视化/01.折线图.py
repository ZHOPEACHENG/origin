from pyecharts.charts import *
import json

# 读取数据
with open('D:/PyCharmProjects/案例资料/折线图数据/美国.txt', 'r', encoding='UTF-8') as f_us:
    data_us = f_us.read()
# 处理数据
data_us = data_us.replace('jsonp_1629344292311_69436(', '')
data_us = data_us[:-2]
data_us = json.loads(data_us)
data_us_trend = data_us['data'][0]['trend']
# 画图
line = Line()
line.add_xaxis(data_us_trend['updateDate'][:314:1])
line.add_yaxis('确诊人数', data_us_trend['list'][0]['data'][:314:1])
line.render()
