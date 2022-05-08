import urllib.request
import urllib.error

import requests
import pandas as pd

# url="https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d"%int(time.time()*1000)
url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'

data = requests.get(url=url).json()['data']["diseaseh5Shelf"]
china_data = data['areaTree'][0]['children']

print(type(data))


data_set = []

for i in china_data:
    data_dict = {}  # dict
    # 地区
    data_dict['province'] = i['name']  # 每个字典name对应的内容
    # 疫情数据
    # 新增确诊
    data_dict['nowConfirm'] = i['total']['nowConfirm']
    # 累计确诊人数
    data_dict['confirm'] = i['total']['confirm']
    # 死亡人数
    data_dict['dead'] = i['total']['dead']
    # 治愈人数
    data_dict['heal'] = i['total']['heal']
    data_set.append(data_dict)  # 追加每个元素
df = pd.DataFrame(data_set)  # liebiao
print(df)
# 保存数据csv
df.to_csv('./data/metadata/国内疫情数据.csv')
