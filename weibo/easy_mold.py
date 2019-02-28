# encoding: utf-8
'''
from nltk.stem.wordnet import WordNetLemmatizer
import stringimport genism
from gensim import corpora

doc1 = "国内综艺界蓬勃发展，多种节目形式日益更新，可是影视圈的套路却一成不变，都2019年IP改编的电视剧依旧是国内电影电视剧的主流，这不，连张艺谋回归小荧幕的作品都选择改编大热小说《遮天》"
doc2 = "OPEC和俄罗斯还在不断的减产试图抬升油价，而远在大洋彼岸的美国却在不断增产原油并快速抢占市场，在利益面前，OPEC+或将提前面临“散伙”的风险"
doc3 = "为了更好地完成东京奥运会任务，中国乒协与男、女队教练组签订了考核及奖惩标准。中国乒协备战东京奥运会总指挥刘国梁介绍：如果男、女队任何一组考核不及格，他都会自罚全年薪酬，誓与团队共进退。"
doc4 = "我很喜欢逛街，买东西"
doc5 = "迪丽热巴好漂亮啊，时尚又可爱，迪丽热巴最棒"
doc_complete = [doc1, doc2, doc3, doc4, doc5]

stopwords = []
f = open("stopword.txt", 'r', encoding='UTF-8')  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
while line:
    line = line.replace('\n', '')
    stopwords.append(line)
    line = f.readline()
f.close()
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]

# 创建语料的词语词典，每个单独的词语都会被赋予一个索引
dictionary = corpora.Dictionary(doc_clean)
# 使用上面的词典，将转换文档列表（语料）变成 DT 矩阵
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# 使用 gensim 来创建 LDA 模型对象
Lda = genism.models.ldamodel.LdaModel
# 在 DT 矩阵上运行和训练 LDA 模型
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

# print(ldamodel.print_topics(num_topics=3, num_words=3))
'''