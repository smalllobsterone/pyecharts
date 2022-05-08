from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd

fp = pd.read_csv('./data/metadata/国内疫情数据.csv', encoding='utf-8')
province = list(fp.province)  # 省份
healRate = list(fp.heal)  # 治愈人数
deadRate = list(fp.dead)  # 死亡人数
diagnosed = list(fp.confirm)  # 确诊人数
# 治愈率改为两位小数，做百分比时
cure_rate = list(map(lambda x: format((x[0] / x[1]) * 100, '.2f'), zip(healRate, diagnosed)))

# 死亡率
mortality_rate = list(map(lambda x: format((x[0] / x[1]) * 100, '.2f'), zip(deadRate, diagnosed)))

try:
    bar = (
        Bar(
            opts.InitOpts(width='1600px', height='600px', page_title="疫情治愈率和死亡率情况")
        )
            .add_xaxis(province)  # 添加x轴数据
            .add_yaxis("治愈率", cure_rate, label_opts=opts.LabelOpts(
            formatter=JsCode("function (params) {return params.value + '%'}")))  # y的数据添加百分号
            .add_yaxis("死亡率", mortality_rate, label_opts=opts.LabelOpts(
            formatter=JsCode("function (params) {return params.value + '%'}")))

            .set_global_opts(title_opts=opts.TitleOpts(title="疫情治愈率和死亡率情况"),
                             yaxis_opts=opts.AxisOpts(type_='value',
                                                      axislabel_opts=opts.LabelOpts(formatter="{value}%"))  # 设置y轴的符号%
                             )

    )
except ZeroDivisionError:
    print('计算出错')
except IOError:
    print('未找到文件')
else:
    bar.render("./data/templates/疫情治愈率和死亡率柱状图.html")
