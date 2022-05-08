import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud

# 数据提取
fp = pd.read_csv('./data/metadata/国内疫情数据.csv', encoding='utf-8')
data_list1 = zip(list(fp.province), list(fp.dead))
new_data = list(data_list1)
c = (
    WordCloud(init_opts=opts.InitOpts(page_title="中国疫情词云图"))
        .add(shape="circle", series_name="中国疫情词云图", data_pair=new_data, word_size_range=[50, 400])
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="中国疫情词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),  # 提示
    )

)
c.render(path='./data/templates/中国疫情词云图.html')
