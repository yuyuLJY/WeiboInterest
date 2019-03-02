# encoding: utf-8
import jieba
import re
import xlrd
import xlwt
from collections import defaultdict # 字典，用于词频统计
from openpyxl import load_workbook#写入exce

def drawPicture():
    print("")

# 返回词的频率和词
def countWord(sentence):
    jieba.add_word('猪猪包')
    jieba.add_word('热巴')
    jieba.add_word('迪丽热巴')
    jieba.add_word('掌心包')
    jieba.add_word("炒鸡")
    jieba.add_word('关晓彤')
    jieba.add_word('口袋魔法')
    jieba.add_word('苏菲')
    # jieba.add_word("烈儿")
    jieba.add_word("天猫旗舰店")
    jieba.add_word("大姨妈")
    jieba.add_word("烈儿")
    jieba.add_word("小猪猪")
    jieba.add_word("姨妈巾")
    jieba.add_word("囤货")
    jieba.add_word("双十一")
    jieba.add_word("双十二")
    jieba.add_word("挺好")
    jieba.add_word("挺划算")
    jieba.add_word("挺新")
    jieba.add_word("双11")
    jieba.add_word("双12")
    word = jieba.lcut(sentence,cut_all=False)
    # 检验分词效果
    for i in range(len(word)):
        print("word:"+ word[i])

    stopwords = []
    f = open("stopword.txt", 'r', encoding='UTF-8')  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        line = line.replace('\n', '')
        stopwords.append(line)
        line = f.readline()
    f.close()
    stopwords.append("\t")
    stopwords.append('哒')
    # print(stopwords.__contains__("！"))
    # print(word.__contains__("少女"))
    # print(word[5].__eq__("好")) # False
    # print(word[5]) # 好
    #print(str(word[5]))
    wordfrequency = defaultdict(int)
    for w in word:
        if w not in stopwords:
            wordfrequency[w] += 1

    for w in wordfrequency:
        print(w+" "+str(wordfrequency[w]))
    return wordfrequency

def writeToExel(wordfrequency):
    '''
    path = "苏菲分词.xlsx"
    # path = "E:/Do it/ZhangXinBao"
    file = load_workbook(path)  # 打开excel
    nsheet = file.create_sheet('frequency', index=0)  # 新建表
    style = xlwt.XFStyle()
    nsheet.cell(1, 1, 'word',style)  # 写入表头
    nsheet.cell(1, 2, 'frequency',style)  # 写入表头

    wordfrequency_order = sorted(wordfrequency.items(), key=lambda x: x[1], reverse=True)  # 把字典按词频降序排列

    for n in range(2, len(wordfrequency_order) + 2):  # 把降序后的词频统计结果写入excel
        nsheet.cell(n, 1, wordfrequency_order[n - 2][0],style)
        nsheet.cell(n, 2, wordfrequency_order[n - 2][1],style)

    file.save(path)
    '''
    print("评论"+str(len(wordfrequency)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#new')
    i = 1
    for w in wordfrequency:
        worksheet.write(i, 0, w, style)  # Outputs 5
        worksheet.write(i, 1, wordfrequency[w])  # Outputs 2
        i = i+1
    workbook.save('掌心包分词1.xls')

def main():
    # 逐行读取文件，并把评论拼接成一个str
    str = " "
    '''
    f = open("苏菲淘宝评价clean.txt",'r', encoding='UTF-8')  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        line = line.replace('\n', '')
        print(line.split("   ")[1])
        str = str + line.split("   ")[1]
        line = f.readline()
    f.close()
    '''
    exfile = xlrd.open_workbook("掌心包粗略评论分词&cleanData.xls")
    sheet1 = exfile.sheet_by_name('RawData')  # 读取Sheet1的内容，根据实际情况填写表名

    n = sheet1.nrows  # 表的总行数
    mytext = ''
    for i in range(1, n):
        text = sheet1.row(i)[1].value  # 从第0行开始计数，第0行是栏目，第1行是要的内容
        mytext = mytext + " " + text  # 把每一天内容合并到一个str中


    print("组合后:"+mytext)
    # fre,word = countWord(str)
    fre = countWord(mytext) # 返回词频字典
    writeToExel(fre)

main()