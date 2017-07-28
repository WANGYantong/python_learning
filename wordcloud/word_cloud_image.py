"""
Image-colored wordcloud
=======================

You can color a word-cloud by using an image-based coloring strategy
implemented in ImageColorGenerator. It uses the average color of the region
occupied by the word in a source image. You can combine this with masking
pure white will be interpreted as 'don't occupy' by the WordCloud object when
passed as mask.
If you want white as a legal color, you can just pass a different image to
"mask",  but make sure the image shapes line up.
"""

import os
import PIL
import numpy as np
import matplotlib.pyplot as plt
import wordcloud

d = os.path.dirname(__file__)
text = open(os.path.join(d, 'alice.txt')).read()
alice_coloring = np.array(PIL.Image.open(os.path.join(d, 'alice_color.png')))

stopwords = set(wordcloud.STOPWORDS)
stopwords.add("said")

wc = wordcloud.WordCloud(background_color="white", max_words=2000,
                         mask=alice_coloring, stopwords=stopwords,
                         max_font_size=40, random_state=42).generate(text)
image_colors = wordcloud.ImageColorGenerator(alice_coloring)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()

plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()

plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
