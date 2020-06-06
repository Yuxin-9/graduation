import os
import xlwt
import wenzhang_Lemmatizer1
from gensim import corpora
from gensim.corpora import Dictionary
from gensim.models.wrappers import LdaMallet
#from gensim.models.coherencemodel import CoherenceModel

#将文档与主题概率分布写入excel
def writedoc_topicToExcleFile(inputData,outPutFile):
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    j = 1
    for i in range(len(inputData)):
        for j in range(len(inputData[i])):
            sheet.write(i, j, str(inputData[i][j]))
    f.save(outPutFile)
    print('数据写入完毕!')

#将主题与词概率分布写入excel
def writetopic_wordToExcleFile(inputData,outPutFile):
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    for i in range(len(inputData)):
        sheet.write(i,0, inputData[i][0])
        sheet.write(i,1, inputData[i][1])
    f.save(outPutFile)
    print('数据写入完毕!')

def txt_to_numpy(filename):#将doc_topic文档转化为矩阵
    doc_topics=[]
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        p_float= []
        p=line.split()
        p_str=p[2:]
        for i in range(len(p_str)):
            p_float.append(float(p_str[i]))
        doc_topics.append(p_float)
    print(filename)
    #print(doc_topics)
    return doc_topics

def main():
    num_topics = 10
    #doc_topics_path='C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\151文章\\mallet模型\\10_3_doctopics.txt'
    MALLET_PATH = os.path.join("D:\Mallet", "mallet-2.0.8", "bin", "mallet.bat")  # r"D:\Mallet\mallet-2.0.8\bin"
    texts = wenzhang_Lemmatizer1.texts2
    dictionary = corpora.Dictionary(texts)
    dictionary.save('dictionary_mallet_10_3.dictionary')
    #dictionary = corpora.Dictionary.load('dictionary_mallet_10_3.dictionary')
    word_id = dictionary.token2id
    corpus = [dictionary.doc2bow(text) for text in texts]
    # corpora.MmCorpus.serialize('corpus_mallet_10_3.mm', corpus)  # 保存corpus
    # corpus = corpora.MmCorpus('corpus_wenzhang.mm')  # 加载
    # print(os.path.abspath('corpus.mm'))
    mallet_lda_model = LdaMallet(mallet_path=MALLET_PATH, corpus=corpus, num_topics=num_topics, id2word=dictionary)
    mallet_lda_model.save('C:\\Users\\asus\\Desktop\\测试\\model\\mallet_lda_model_10_3.model')
    #mallet_lda_model = LdaMallet.load('C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\151文章\\mallet模型\\mallet_lda_model_10_3.model')
    topic_words20 = mallet_lda_model.show_topics(num_topics=num_topics, num_words=20)
    # print(topic_words20)
    writetopic_wordToExcleFile(topic_words20,'C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\151文章\\topic_words20_10_3.xls')
    topic_words = mallet_lda_model.get_topics()
    print(len(topic_words), len(topic_words[0]))
    doc_topics = txt_to_numpy(mallet_lda_model.fdoctopics()) #doc_topics_path
    #print(mallet_lda_model.fdoctopics())
    writedoc_topicToExcleFile(doc_topics,'C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\151文章\\doc_topics20_10_3')
    return texts, word_id, topic_words, doc_topics, num_topics

texts, word_id, topic_words, doc_topics, num_topics = main()

'''
    MALLET_PATH = os.path.join("D:\Mallet", "mallet-2.0.8", "bin", "mallet.bat")
    texts = wenzhang_Lemmatizer1.texts2
    for num_topics in range(11,21,1):
        dictionary = corpora.Dictionary(texts)
        dictionary_path='dictionary_mallet122_'+str(num_topics)+'.dictionary'
        dictionary.save(dictionary_path)
        corpus = [dictionary.doc2bow(text) for text in texts]
        mallet_lda_model=LdaMallet( mallet_path=MALLET_PATH, corpus=corpus, num_topics=num_topics, id2word=dictionary)
        mallet_path='C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\122文章\\mallet模型\\dictionary_mallet122_'+str(num_topics)+'.model'
        mallet_lda_model.save(mallet_path)
        topic_words20 = mallet_lda_model.show_topics(num_topics=num_topics, num_words=20)
        topic_words20_path='C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\122文章\\topic_words_'+str(num_topics)+'.xls'
        writetopic_wordToExcleFile(topic_words20,topic_words20_path)
        topic_words=mallet_lda_model.get_topics()
        print(len(topic_words),len(topic_words[0]))
        doc_topics = txt_to_numpy(mallet_lda_model.fdoctopics())
        doc_topics_path = 'C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\122文章\\doc_topics_' + str(num_topics) + '.xls'
        writedoc_topicToExcleFile(doc_topics,doc_topics_path)
    print('完成!')
    return texts,topic_words,doc_topics,num_topics


'''