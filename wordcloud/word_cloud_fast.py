import wordcloud
import matplotlib.pyplot as plt

path_txt = "/home/thinker/PycharmProjects/python_learning/wordcloud/alice.txt"
f = open(path_txt, 'r').read()
result = wordcloud.WordCloud(background_color="white",
                             width=1000,
                             height=860,
                             margin=2).generate(f)

plt.imshow(result)
plt.axis("off")
plt.show()

wordcloud.to_file("fast.png")
