#分词
import  jieba
with open('十九大.txt', errors='ignore') as f:
    s = f.read()
word_list = list(jieba.cut(s))
print('分词总数:', len(word_list))
#print('示例：', word_list)

#统计词频
from collections import Counter
words_count = Counter(word_list)
most_words = words_count.most_common(128)
#print(most_words)
#去除符号介词助词
most_words = [words for words in most_words if words[0] not in '，。、“”（）！；的和是在要为以把了对中到有上不等更二从大\n\u3000']
print(most_words)

#wordclound
dict_words = {}
for words in most_words:
    dict_words[words[0]] = words[1]
from wordcloud import WordCloud, ImageColorGenerator

#读取图片
from scipy.misc import imread
bg_pic = imread('report19.png')
#配置词云参数
wc = WordCloud(
    font_path='STXINWEI.TTF',
    background_color='red',
    mask=bg_pic,
    max_font_size=100,
)

#生成词云
wc.generate_from_frequencies(dict_words)
image_colors = ImageColorGenerator(bg_pic)
wc.recolor(color_func=image_colors)

import matplotlib.pyplot as plt
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('word_freq.jpg')

