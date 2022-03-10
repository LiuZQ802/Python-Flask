"""
创建词云图片
"""

from wordcloud import WordCloud
import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图，数据可视化
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import re
import pymysql

con = pymysql.connect(host='localhost', user='root', password='root', db='douban')
cursor = con.cursor()
sql = 'select instroduction from movie250'
cursor.execute(sql)
data = cursor.fetchall()  # 从数据库取数据
text = ''
for item in data:
    da = re.sub(r'[，|。|\s|.]', '', item[0])  # 将数据去掉句号空格等，得到纯文字
    text = text + da
cursor.close()
con.close()
# jieba库将一大串文字分成一个个词
cut = jieba.cut(text)
string = ' '.join(cut)
# print(len(string))

# 绘图
img = Image.open(r'./static/assets/img/images.jpg')
img_arry = np.array(img)  # 将图片转换为数组 ,用numpy库
wc = WordCloud(
    background_color='white',  # 背景颜色
    mask=img_arry,  # 遮罩的图片
    font_path="msyh.ttc"  # 设置字体
)
wc.generate_from_text(string)  # 从哪个文本生成wc

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 是否显示坐标轴
# plt.show()  #显示图片
plt.savefig(r'./static/assets/img/ciyun.jpg')  # 保存图片
