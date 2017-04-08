#!/usr/bin/env python

from os import path
from wordcloud import WordCloud, STOPWORDS


d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, '../latex/excel/list_ArticleTitles.csv')).read()


stopwords = set(STOPWORDS)

# Generate a word cloud image
# wordcloud = WordCloud(background_color="white"
#             , max_words=200
#             ,stopwords=stopwords
#             ,max_font_size=40
#             ,width = 1000
#             ,height = 500
#             ,relative_scaling=0.1
#             )

wordcloud = WordCloud(background_color="white"
    ,max_font_size=40
    ,width = 400
    ,height = 200
    )
wordcloud.generate(text)

# # Display the generated image:
# # the matplotlib way:
# import matplotlib.pyplot as plt
# plt.imshow(wordcloud)
# plt.axis("off")

# # lower max_font_size
# figure1 = plt.figure()
# plt.imshow(wordcloud, cmap='bone')
# plt.axis("off")
# #plt.show()

# figure1.set_dpi(200)

# plt.savefig('../latex/wordcloudtitles.png',format='png',transparent=True, bbox_inches='tight', pad_inches=0)

wordcloud.to_file(path.join(d, '../latex/wordcloudtitles.png'))


