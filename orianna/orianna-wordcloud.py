from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from numpy._distributor_init import NUMPY_MKL
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import json

d = path.dirname(__file__)

txt_freq= open(path.join(d, 'data-orianna.txt')).read()

alice_coloring = imread(path.join(d, "alice_color.png"))

wc = WordCloud(background_color="white",mask=alice_coloring,stopwords=STOPWORDS.add("said"),max_font_size=100,random_state=42)

txt_freq=json.loads(txt_freq)
wc.generate_from_frequencies(txt_freq)

image_colors = ImageColorGenerator(alice_coloring)


plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()