import requests
import pandas as pd
from pyecharts.charts import Line  # 折线图
from pyecharts import options as opts

# chinaDayList下每日累计确诊爬取数据
url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
resp = requests.post(url)

data_set2 = []
for i in resp.json()['data']['chinaDayList']:
    data_dict = {'date': i['date'], 'confirm': i['confirm']}  # 获取对应的键值对
    data_set2.append(data_dict)
print(data_set2)
df = pd.DataFrame(data_set2)
df.to_csv('./data/metadata/2月以来的国内疫情趋势.csv')  # 存入csv

# 数据提取部分
fp = pd.read_csv('./data/metadata/2月以来的国内疫情趋势.csv', encoding='utf-8')
date2 = list(fp.date)  #
newdate2 = [str(i) for i in date2]  # 没有这个折线图会乱
confirm = list(fp.confirm)
print(newdate2)
print(confirm)
# 绘制折线图
line = (
    Line(init_opts=opts.InitOpts(width='1720px', height='720px', page_title="中国疫情近两月趋势"))  # 设置画布大小
        .add_xaxis(newdate2)
        .add_yaxis('中国近每日累计病例', confirm, is_smooth=True)  # 平滑显示
        .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情趋势（每日累计确诊人数）"),
                         tooltip_opts=opts.TooltipOpts(trigger="axis"))  # 准星提示
)
line.render(path='./data/templates/2月以来的国内疫情趋势.html')  # render 会生成本地 HTML 文件
