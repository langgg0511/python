from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = open('news.txt', 'r').read()
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('test.jpg')
