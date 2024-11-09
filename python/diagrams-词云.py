import jieba
import wordcloud
# 读取文本
with open("txt文件路径",encoding="utf-8") as f:
    s = f.read()
print(s)
#ls = jieba.lcut(s) # 生成分词列表
#text = ' '.join(ls) # 连接成字符串


#stopwords = ["的","是","了"] # 去掉不需要显示的词

wc = wordcloud.WordCloud(font_path="/System/Library/Fonts/PingFang.ttc",
                        width = 1920,
                         height = 1080,
                         background_color='white',
                         max_words=500,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(s) # 加载词云文本
wc.to_file("/Volumes/expand for Daaihou/截图/cy1.png") # 保存词云文件

#以txt文本为例，其余格式需按需修改
