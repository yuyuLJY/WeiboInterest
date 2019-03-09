# encoding: utf-8
from gensim.models import word2vec

def readTopic():
    sentences = word2vec.Text8Corpus(u'E:/Do it/ZhangXinBao/weibo/topics.txt')
    #model = word2vec.Word2Vec(sentences, min_count=1)
    #sentences = [["干净", "水", "清泉", "可乐", "矿泉水", '干净','清泉','泉水','清泉'], ['鸡腿', '猪腿', '烤鸭', '烧鸭']]
    #sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
    model = word2vec.Word2Vec(sentences, min_count=1)

    # y2 = model.similarity(u"好", u"还行")
    # print(y2)

    for i in model.most_similar(u"周小晨"):
        print(i[0]+" "+ str(i[1]))

def main():
    readTopic()

main()