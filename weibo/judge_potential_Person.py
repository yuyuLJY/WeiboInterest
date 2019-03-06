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
from gensim import corpora, models, similarities

#TODO 计算本文列表
def computeWordList( wordList,id,stop_words_dict,good_list):
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

    score_4 = 0  #微博条数
    score_5 = 0  #提及产品
    score_6 = 0  #@护舒宝
    print("ID: "+id)
    exfile = xlrd.open_workbook("E:/Do it/ZhangXinBao/数据/收集数据/旅游日记/评论/" + id + ".xls")
    sheet1 = exfile.sheet_by_name('#')  # 读取Sheet1的内容，根据实际情况填写表名

    n = sheet1.nrows  # 表的总行数
    if n > 300:
        score_4 = 10
    for i in range(0, n):
        text = ''
        text = sheet1.row(i)[1].value  # 从第0行开始计数，第0行是栏目，第1行是要的内容
        #只有没得分的才进行判断
        if score_6==0:
            if text.__contains__('护舒宝'):
                score_6 = 15
        if score_5==0:
            for jj in good_list:
                if text.__contains__(jj):
                    score_5 = 15
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

    return score_4,score_5,score_6
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
        #for i in topic.argsort()[:-n_top_words - 1:-1]:
            #print(feature_names[i])
            #all_word_list.append(feature_names[i])
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

    print()

def three_vec():
    #TODO 读取三个文件的词，分别对应 时尚list_1, 旅行list_2, 萌宠list_3,并加入texts
    # 读取时尚文档
    list_1 = []  #时尚
    list_2 = []  #旅游
    list_3 = []  #萌宠
    f = open("E:/Do it/ZhangXinBao/数据/使用数据/时尚.txt")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        #print(line)
        line = line.replace('\n', '')
        list_1.append(line)
        line = f.readline()
    f.close()
    print(len(list_1))
    #list_1 = ['美妆','化妆刷','美拍']

    f = open("E:/Do it/ZhangXinBao/数据/使用数据/旅游.txt")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        #print(line)
        line = line.replace('\n', '')
        list_2.append(line)
        line = f.readline()
    f.close()

    f = open("E:/Do it/ZhangXinBao/数据/使用数据/萌宠少女感.txt")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        #print(line)
        line = line.replace('\n', '')
        list_3.append(line)
        line = f.readline()
    f.close()

    texts = [list_1, list_2, list_3]

    #main_interest = ['美妆', '仙女', '阳光', '潘那白', '巴黎时装周']
    #texts = [['美妆', '时尚', '美妆', '粉底', '护肤', '神仙发色', '美妆', '粉底液', '遮瑕膏', '技巧', '照片', ' 漂亮', '深夜徐老师 ', '博妞', '化妆'],
    #         ['旅游', '拍照', '技术', '世界', '行走', '潘那白']]
    # print(texts)
    return texts

def judge_interest_similar(texts,main_interest,score):
    '''

    :param texts:
    :param main_interest:
    :return:
    '''

    interest = main_interest.split(' ')
    for i in interest:
        if texts[0].__contains__(i):
            score_1 = 50
            break
        if texts[1].__contains__(i):
            score_2 = 50
            break
        if texts[2].__contains__(i):
            score_3 = 50
            break
    return score_1,score_2,score_3
    '''
    print(main_interest)
    dictionary = corpora.Dictionary(texts)
    feature_cnt = len(dictionary.token2id)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    new_vec = dictionary.doc2bow(main_interest)
    # 相似度计算
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
    sim = index[tfidf[new_vec]]
    for i in range(len(sim)):
        print('第', i + 1, '句话的相似度为：', sim[i])    
    '''
def writeScoreToexcel(id,score):
    print("评论"+str(len(score)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#')
    worksheet.write(0, 0, '基础分', style)
    worksheet.write(0, 1, '时尚', style)
    worksheet.write(0, 2, '旅行', style)
    worksheet.write(0, 3, '萌宠可爱', style)
    worksheet.write(0, 4, '微博活跃度', style)
    worksheet.write(0, 5, '提及产品', style)
    worksheet.write(0, 6, '@护舒宝', style)
    for i in range(1,len(score)):
        worksheet.write(i, 0, score[i]['基本分'], style)
        worksheet.write(i, 1, score[i]['时尚'], style)
        worksheet.write(i, 2, score[i]['旅行'], style)
        worksheet.write(i, 3, score[i]['萌宠可爱'], style)
        worksheet.write(i, 4, score[i]['微博状态活跃'], style)
        worksheet.write(i, 5, score[i]['提及产品'], style)
        worksheet.write(i, 6, score[i]['@ 护舒宝'], style)
    workbook.save('E:/Do it/ZhangXinBao/数据/收集数据/旅游日记/旅游日记_潜在用户'+'.xls')


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

# 得到两个话题筛选出来的有效ID
def getAvalidID(avalidID):
    exfile = xlrd.open_workbook("E:/Do it/ZhangXinBao/数据/收集数据/旅游日记/ID信息.xlsx")
    sheet1 = exfile.sheet_by_name('Sheet1')  # 读取Sheet1的内容，根据实际情况填写表名

    n = sheet1.nrows  # 表的总行数
    for i in range(1, n):
        text = sheet1.row(i)[2].value  # 从第0行开始计数，第0行是栏目，第1行是要的内容
        # //weibo.com/1796405533?refer_flag=1001030103_
        cleanText = re.findall(r'[0-9]+', text)[0]
        if not avalidID.__contains__(cleanText):
            avalidID.append(cleanText)

def main():
    #TODO score[0] 基础分
    #TODO score[1] 兴趣分-时尚
    # TODO score[2] 兴趣分-旅行
    # TODO score[3] 兴趣分-萌宠
    #TODO score[4] 发微博的数量
    #TODO score[5] 提及产品
    #TODO score[6] @护舒宝
    score = []
    score_0 = 10
    wordList = []  # 该论模型的训练样本
    avalidID = []
    stop_words_dict = []  # 停用词词库
    n_top_words = 10  # 提取几个关键词
    all_word_list = []  # 统计所有的主题词
    good_list = ['液体卫生巾','有机纯棉','考拉','云感棉','瞬洁','小云窗','超值干爽','掌心包']
    prepare(stop_words_dict)
    texts = three_vec()
    # TODO 得到用户的ID
    #getAvalidID(avalidID)
    avalidID =['5697069584']
    #avalidID = ['美妆', '时尚', '旅游']
    for i in range(len(avalidID)):
        print(avalidID[i])
        score_4, score_5, score_6 = computeWordList(wordList, avalidID[i], stop_words_dict,good_list)  # 获取词的列表
        print(str(score_4)+" "+str(score_5)+" "+str(score_6))
        word_frequency_mat, feature_names = computeWordFrequency(wordList)  # 计算词的频率
        tfidf_mat = computeTFIDF(word_frequency_mat)  # 计算TF-IDF
        lda = LDA(tfidf_mat)
        main_interest = print_top_words(lda, feature_names, n_top_words)  # 获取用户的兴趣词
        print(main_interest)
        #score_1, score_2, score_3 = judge_interest_similar(texts, main_interest)
        #score.append({'基本分':score_0,'时尚':score_1,'旅行':score_2,'萌宠可爱':score_3,'微博状态活跃':score_4,'提及产品':score_5,'@护舒宝':score_6})
        wordList.clear()  # 本次使用的单词列表清空

    for j in all_word_list:
        print(j)

    print("")

main()