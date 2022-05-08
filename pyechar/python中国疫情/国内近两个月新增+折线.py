import requests
import pandas as pd
from pyecharts.charts import Line  # 折线图
from pyecharts import options as opts

url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
resp = requests.post(url)

data_set = []
for i in resp.json()['data']['chinaDayAddList']:
    data_dict = {'date': i['date'], 'confirm': i['confirm']}  # 获取对应的键值对
    data_set.append(data_dict)
print(data_set)
df = pd.DataFrame(data_set)
df.to_csv('./data/metadata/国内近两个月新增确诊数数据.csv')

# 数据提取部分
fp = pd.read_csv('./data/metadata/国内近两个月新增确诊数数据.csv', encoding='utf-8')
date = list(fp.date)  #
newdate = [str(i) for i in date]  # 没有这个折线图会乱
confirm = list(fp.confirm)
print(newdate)
print(confirm)
# 绘制折线图
line = (
    Line(init_opts=opts.InitOpts(width='1720px', height='720px', page_title="中国疫情新增折线图"))  # 设置画布大小
        .add_xaxis(newdate)
        .add_yaxis('中国新增病例', confirm)
        .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情基本示例"),
                         tooltip_opts=opts.TooltipOpts(trigger="axis"))  # 设置准星
)
line.render(path='./data/templates/中国疫情新增折线图.html')  # render 会生成本地 HTML 文件
