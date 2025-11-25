from pyecharts.charts import *
import json
from pyecharts.options import *
import pyecharts.globals as glb

class Visualizer:


    def line(self,name1,name2,name3 ):


        # 读取数据
        f1 = open(f'D:/PyCharmProjects/案例资料/折线图数据/{name1}.txt', 'r', encoding='UTF-8')
        f2 = open(f'D:/PyCharmProjects/案例资料/折线图数据/{name2}.txt', 'r', encoding='UTF-8')
        f3 = open(f'D:/PyCharmProjects/案例资料/折线图数据/{name3}.txt', 'r', encoding='UTF-8')
        data1 = f1.read()
        data2 = f2.read()
        data3 = f3.read()
        # 处理数据
        x1 = data1.index('{')
        x2 = data2.index('{')
        x3 = data3.index('{')
        data1 = data1[x1:-2]
        data2 = data2[x2:-2]
        data3 = data3[x3:-2]

        data1 = json.loads(data1)
        data2 = json.loads(data2)
        data3 = json.loads(data3)

        data1_trend = data1['data'][0]['trend']
        data2_trend = data2['data'][0]['trend']
        data3_trend = data3['data'][0]['trend']
        # 画图
        line = Line()

        line.add_xaxis(data1_trend['updateDate'][:314:1])

        line.add_yaxis(f'{name1}确诊人数', data1_trend['list'][0]['data'][:314:1],label_opts=LabelOpts(is_show=False))
        line.add_yaxis(f'{name2}确诊人数', data2_trend['list'][0]['data'][:314:1],label_opts=LabelOpts(is_show=False))
        line.add_yaxis(f'{name3}确诊人数', data3_trend['list'][0]['data'][:314:1],label_opts=LabelOpts(is_show=False))
        line.set_global_opts(
            title_opts=TitleOpts(title=f'{name1},{name2},{name3}确诊人数趋势图',pos_left = 'center',pos_bottom = "1%")

        )




        line.render('各国确诊人数.html')

a = Visualizer()
a.line('美国','印度','日本')