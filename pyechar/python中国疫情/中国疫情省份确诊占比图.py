import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

fp = pd.read_csv('./data/metadata/国内疫情数据.csv', encoding='utf-8')
province = list(fp.province)  # 词
# print(province)
confirm = list(fp.confirm)

# print(confirm)
(
    Pie(init_opts=opts.InitOpts(width='1440px', height='920px', page_title="中国疫情省份确诊占比图"))  # 默认900，600
        .add(series_name='', label_opts=opts.LabelOpts(is_show=True, formatter='{d}%')
             , data_pair=[(j, i) for i, j in zip(confirm, province)], rosetype='radius')  # 南丁格尔图
).render("./data/templates/中国疫情省份确诊占比图.html")
