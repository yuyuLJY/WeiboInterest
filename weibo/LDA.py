# encoding: utf-8
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer, TfidfVectorizer
import requests
import re
from bs4 import BeautifulSoup
import time
import bs4
import xlwt
import xlrd
import jieba
import nltk
from nltk.stem.porter import PorterStemmer

#TODO 计算本文列表
def computeWordList( wordList,id,stop_words_dict):
    '''
    （1）读取停用词的词库和准备好的词库（2）再读取评论的文件（3）分词整理输入wordList
    :param stop_word_path:
    :param comment_path:
    :param wordList:
    :return:
    '''
    #comment_list = ['1876693235','1978351291','619880505','1428990944','1743027543','735658915','1562697291','1601455762',
     #               '1634059993','523790789','1783376715','2007283277']
    #comment_list=['523790789']

    print("ID: "+id)
    exfile = xlrd.open_workbook("E:/Do it/ZhangXinBao/weibo/comment/" + id + ".xls")
    sheet1 = exfile.sheet_by_name('#')  # 读取Sheet1的内容，根据实际情况填写表名

    n = sheet1.nrows  # 表的总行数
    for i in range(0, n):
        text = ''
        text = sheet1.row(i)[1].value  # 从第0行开始计数，第0行是栏目，第1行是要的内容
        # print("原来的句子: "+text)
        #TODO 替换掉字母和数字
        text = re.sub('[a-zA-Z0-9]', '', text)  # 只除去数字，因为有些美妆博主的名字有英文
        # print("处理后的句子: "+text)
        #TODO  分词
        words = jieba.lcut(text)
        #TODO 去停用词
        words_1 = [w for w in words if w not in stop_words_dict and len(w) > 1]
        #TODO 仅保留名词或特定POS
        refiltered = nltk.pos_tag(words_1)
        words_2 = [w for w, pos in refiltered if pos.startswith('NN')]
        #TODO 词干化
        ps = PorterStemmer()
        words_3 = [ps.stem(w) for w in words_2]
        join_all_words = ' '.join(words_3)
        # print("用空格隔开：" + join_all_words)
        wordList.append(join_all_words)

    '''
    wordList.append("猫 狗 猪 小狗 猪 小猪")
    wordList.append("郁金香 郁金香 百合")
    wordList.append("牛肉 火腿  鸡肉")
    wordList.append("精华  鸡肉")
    wordList.append("可乐 柠檬 鸡肉 鸡肉 鸡肉")
    wordList.append("铅笔盒 迪丽热巴 迪丽热巴 迪丽热巴")  # 热巴这个词很重要
    '''

def  computeWordFrequency(wordList):
    '''
    将文本列表转换成词频矩阵，CountVectorizer可以做到
    :param wordList:文本列表
    :return:词频矩阵
    '''
    # print(wordList)
    # min_df = 3
    c_vectorizer = CountVectorizer(max_df=0.90, min_df = 2,max_features=150)
    word_frequency_mat = c_vectorizer .fit_transform(wordList)
    feature_names = c_vectorizer.get_feature_names()
    #print(c_vectorizer.vocabulary_)
    return word_frequency_mat, feature_names
    #print(word_frequency_mat)

def computeTFIDF(word_frequency_mat):
    '''
    词频矩阵转换为TF-IDF矩阵，使用TfidfTransformer
    :param word_frequency_mat:词频矩阵
    :return: TF-IDF矩阵
    '''
    tfidf_vectorizer = TfidfTransformer()
    tfidf_mat = tfidf_vectorizer.fit_transform(word_frequency_mat)
    print(tfidf_mat)  # 打印出TF-IDF值
    return tfidf_mat

def LDA(tfidf_mat):
    '''
    :param tfidf_mat:词频-逆文本频率
    :return: lda模型
    '''
    # 主题个数和迭代次数
    lda_model = LatentDirichletAllocation(n_components=1, max_iter=500,learning_method='batch')
    # 使用TF-IDF矩阵拟合LDA模型
    lda_model.fit(tfidf_mat)  # 用TF-IDF的值来训练关键词的重要程度

    # 拟合后模型的实质
    #print(lda_mat)
    print(lda_model.perplexity(tfidf_mat))
    return lda_model

#把主题词打印出来？？？？
def print_top_words(lda, feature_names, n_top_words,all_word_list):
    '''

    :param model: lda模型
    :param feature_names:
    :param n_top_words:取多少个词语
    :return:
    '''
    for topic_idx, topic in enumerate(lda.components_):
        print("Topic #%d:" % topic_idx)
        for i in topic.argsort()[:-n_top_words - 1:-1]:
            #print(feature_names[i])
            all_word_list.append(feature_names[i])
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

    print()

# 得到两个话题筛选出来的有效ID
def getAvalidID(avalidID):
    exfile = xlrd.open_workbook("C:/Users/yuyu/Desktop/宝洁challenge/复赛/数据/cleanData/#掌心包话题用户ID.xlsx")
    sheet1 = exfile.sheet_by_name('Sheet1')  # 读取Sheet1的内容，根据实际情况填写表名

    n = sheet1.nrows  # 表的总行数
    for i in range(1, n):
        text = sheet1.row(i)[2].value  # 从第0行开始计数，第0行是栏目，第1行是要的内容
        # //weibo.com/1796405533?refer_flag=1001030103_
        cleanText = re.findall(r'[0-9]+', text)[0]
        if not avalidID.__contains__(cleanText):
            avalidID.append(cleanText)

def prepare(stop_words_dict):

    # 添加结巴分词的词库
    words_dict_path = "E:/Do it/ZhangXinBao/weibo/词库.txt"
    jieba.load_userdict(words_dict_path)

    # 添加停用词
    f = open("E:/Do it/ZhangXinBao/weibo/stopword_comment.txt", 'r', encoding='UTF-8')  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        line = line.replace('\n', '')
        stop_words_dict.append(line)
        line = f.readline()
    f.close()


def main():
    wordList = []  # 该论模型的训练样本
    avalidID =[]
    stop_words_dict = []  # 停用词词库
    n_top_words = 10  # 提取几个关键词
    all_word_list = []  # 统计所有的主题词
    prepare(stop_words_dict)
    #TODO 得到用户的ID
    getAvalidID(avalidID)
    avalidID = ['5697069584']
    #avalidID = ['kyutomo','6341060674','3950978005','5697069584','6080087830','6416496314','5159012441','1601455762',
    #             '1634059993','523790789','1783376715','2007283277']
    for i in range(len(avalidID)):
            print(avalidID[i])
            computeWordList(wordList, avalidID[i], stop_words_dict)  # 获取词的列表
            word_frequency_mat, feature_names = computeWordFrequency(wordList)  # 计算词的频率
            tfidf_mat = computeTFIDF(word_frequency_mat)  # 计算TF-IDF
            lda = LDA(tfidf_mat)
            print_top_words(lda, feature_names, n_top_words, all_word_list)
            wordList.clear()
    for j in all_word_list:
        print(j)
main()