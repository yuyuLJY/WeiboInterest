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

#TODO 计算本文列表
def computeWordList(stop_word_path, comment_path, wordList):
    '''
    （1）读取停用词的词库和准备好的词库（2）再读取评论的文件（3）分词整理输入wordList
    :param stop_word_path:
    :param comment_path:
    :param wordList:
    :return:
    '''
    comment_list = ['1876693235','1978351291','619880505','1428990944','1743027543','735658915','1562697291','1601455762',
                    '1634059993','523790789','1783376715','2007283277']
    mytext = ''
    for i in range(len(comment_list)):
        exfile = xlrd.open_workbook("weibo/comment/"+comment_list[i]+".xls")
        sheet1 = exfile.sheet_by_name('#')  # 读取Sheet1的内容，根据实际情况填写表名

        n = sheet1.nrows  # 表的总行数
        for i in range(0, n):
            text = sheet1.row(i)[1].value  # 从第0行开始计数，第0行是栏目，第1行是要的内容
            mytext = mytext + " " + text  # 把每一天内容合并到一个str中

    print("组合后:"+mytext)
    mytext = re.sub('[a-zA-Z0-9]','',mytext)

    words_dict_path = "weibo/词库.txt"
    jieba.load_userdict(words_dict_path)
    word = jieba.lcut(mytext)



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
    print(wordList)
    c_vectorizer  = CountVectorizer()
    word_frequency_mat = c_vectorizer .fit_transform(wordList)
    feature_names = c_vectorizer.get_feature_names()
    print(c_vectorizer.vocabulary_)
    print(word_frequency_mat)
    return word_frequency_mat, feature_names

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

def IDA(tfidf_mat):
    '''

    :param tfidf_mat:词频-逆文本频率
    :return: lda模型
    '''
    # 主题个数和迭代次数
    lda_model = LatentDirichletAllocation(n_components=2, max_iter=1000)
    # 使用TF-IDF矩阵拟合LDA模型
    lda_model.fit(tfidf_mat)  # 用TF-IDF的值来训练关键词的重要程度

    # 拟合后模型的实质
    #print(lda_mat)
    return lda_model

#把主题词打印出来？？？？
def print_top_words(lda, feature_names, n_top_words):
    '''

    :param model: lda模型
    :param feature_names:
    :param n_top_words:取多少个词语
    :return:
    '''
    for topic_idx, topic in enumerate(lda.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


def main():
    wordList = []
    computeWordList(wordList)   # 获取词的列表
    word_frequency_mat, feature_names = computeWordFrequency(wordList)  # 计算词的频率
    tfidf_mat = computeTFIDF(word_frequency_mat)  # 计算TF-IDF
    lda = IDA(tfidf_mat)
    n_top_words = 2   # 提取几个关键词
    print_top_words(lda, feature_names, n_top_words)
main()