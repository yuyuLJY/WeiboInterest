# encoding: utf-8
import jieba
import re

def drawPicture():
    print("")

# 返回词的频率和词
def countWord(sentence):
    word = jieba.cut(sentence)
    print(' '.join(word))
    for i in range(len(word)):
        print("word:"+ word[i])

def main():
    # 逐行读取文件，并把评论拼接成一个str
    str = ""
    f = open("cleanData.txt")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        print (line.split("   ")[1])
        str = str + line.split("   ")[1]
        line = f.readline()
    f.close()
    print(str)
    # fre,word = countWord(str)
    countWord(str)

main()