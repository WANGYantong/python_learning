import wordcloud
import matplotlib.pyplot as plt
import platform

if platform.platform().startswith("Windows"):
    path_txt =  "C://Users/Thinker/Documents/Projects/python/python_learning/wordcloud/alice.txt"
else:
    path_txt = "/home/thinker/PycharmProjects/python_learning/wordcloud/alice.txt"
f = open(path_txt, 'r').read()
result = wordcloud.WordCloud(background_color="white",
                             width=1000,
                             height=860,
                             margin=2).generate(f)

plt.imshow(result)
plt.axis("off")
plt.show()

result.to_file("fast.png")
