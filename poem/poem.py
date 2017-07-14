import random
import os

path = "C://Users/Thinker/Documents/Projects/python/python_learning/poem/古诗.txt"

poemTitle = [0 for x in range(10)]
poemDynasty = [0 for x in range(10)]
poemAuthor = [0 for x in range(10)]
poemText = [[0 for x in range(10)] for y in range(10)]

INDEXNUM = 0
INDEXTEXT = 0
EMPTYLINE = 0
STATEFLAG = 0

def processTitle(line):
    global poemTitle, poemDynasty, poemAuthor

    indexTitle1 = line.find('【')
    indexTitle2 = line.find('】')
    poemTitle[INDEXNUM] = line[indexTitle1+1:indexTitle2]

    indexDynasty1 = line.find('（')
    indexDynasty2 = line.find('）')
    poemDynasty[INDEXNUM] = line[indexDynasty1+1:indexDynasty2]

    poemAuthor[INDEXNUM] = line[indexDynasty2+1:]


def processText(line):
    global INDEXTEXT, poemText

    if line != '':
        poemText[INDEXNUM][INDEXTEXT] = line
        INDEXTEXT += 1


def processEnd():
    global INDEXNUM, INDEXTEXT
    INDEXNUM += 1
    INDEXTEXT = 0


def analyzeText(line):
    global EMPTYLINE, STATEFLAG

    if line == '':
        EMPTYLINE += 1

    while(True):
        if STATEFLAG == 0:
            if(('诗' in line) or ('词' in line)) and ('【' in line):
                STATEFLAG = 1
            else:
                return

        if STATEFLAG == 1:
            processTitle(line)
            STATEFLAG = 2
            EMPTYLINE = 0
            return

        if STATEFLAG == 2:
            if EMPTYLINE >= 1:
                processEnd()
                STATEFLAG = 0
                EMPTYLINE = 0
                return
            elif (('诗' in line) or ('词' in line)) and ('【' in line):
                processEnd()
                STATEFLAG = 1
                EMPTYLINE = 0
            else:
                processText(line)
                return

def printText(point):
    i = 0
    while(poemText[point][i] != 0):
        print("{}".format(poemText[point][i]))
        i += 1


def lookAround():
    point = random.randrange(0, 10)
    print("【{}】 （{}） {} ".format(poemTitle[point], poemDynasty[point], \
                                 poemAuthor[point]))
    printText(point)


def recite():
    point = random.randrange(0, 10)
    mode = random.randrange(1, 3)
    if mode == 1:
        print("根据题目，说出朝代、作者和诗词内容：")
        print("【{}】".format(poemTitle[point]))
        print("敲击任意键显示答案")
        input()
        print("【{}】 （{}） {} ".format(poemTitle[point], poemDynasty[point], \
                                     poemAuthor[point]))
        printText(point)
    else:
        print("请说出下面这首诗的题目、朝代和作者：")
        printText(point)
        input()
        print("敲击任意键显示答案")
        print("【{}】 （{}） {} ".format(poemTitle[point], poemDynasty[point], \
                                     poemAuthor[point]))

with open(path, encoding="UTF-8") as text:
    for line in text:
        line = line.rstrip().lstrip()
        analyzeText(line)

print("***********************")
print("欢迎来到诗词荣耀！")
print("***********************")
print("请选择模式：")
while(True):
    print("1.随便看看    2.我要挑战    3.退出")
    print('')
    result = input()
    if result == '1':
        lookAround()
        input()
        os.system('cls')
        print("接下来你希望：")
    elif result == '2':
        recite()
        input()
        os.system('cls')
        print("接下来干点儿啥：")
    elif result == '3':
        print("再见！")
        break
    else:
        print("输入错误！请重新选择：")

