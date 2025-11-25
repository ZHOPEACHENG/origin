import json
import pyecharts.options as opts
from pyecharts.charts import Map


# 准备数据
f = open('D:/PyCharmProjects/案例资料/地图数据/疫情.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
data_dict = json.loads(data)
list_area = []
for name in data_dict['areaTree'][0]['children']:
    list_area.append(name['name'])

list_value = []
for value in data_dict['areaTree'][0]['children']:
    list_value.append(value['total']['confirm'])
list =[]
for i in range(0,len(list_area)):
    list.append((list_area[i], list_value[i]))




print(list)
# 绘制地图
map = Map()
map.add( '疫情地图', list, 'china')

map.set_global_opts(
    title_opts=opts.TitleOpts(title="疫情地图"),
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 100000, "color": "#006600"},
            {"min": 50000, "max": 100000, "color": "#FFDE33"},
            {"min": 10000, "max": 50000, "color": "#FFA07A"},
            {"min": 1000, "max": 10000, "color": "#FF4500"},
            {"max": 1000, "color": "#9932CC"}
        ])

)


map.render()









