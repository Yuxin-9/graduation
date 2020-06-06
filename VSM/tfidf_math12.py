#为什么有些词还是没去掉，如' ',anyone等
#常规tfidf计算,可评估单篇文章主题,其中log的底数默认为e
import math
import os
import operator
import exceltolist_wenzhang_tfidf
import exceltolist_wenti_tfidf
import wenti_Lemmatizer
import wenzhang_Lemmatizer
import xlwt


def freqword(wordlis): # 统计单篇词频，并返回字典
  freword = {}
  for i in wordlis:
    if str(i) in freword:
      count = freword[str(i)]
      freword[str(i)] = count+1
    else:
      freword[str(i)] = 1
  #print(freword)
  return freword


def wordinfilecount(word, corpuslis):  # 查出包含该词的文档数，返回数值
    count = 0  # 计数器
    for i in corpuslis:
        if word in set(i):  # 只要文档出现该词，这计数器加1，所以这里用集合
           count = count + 1
        else:
           continue
    #print(word,count)
    return count


def tf_idf(wordlis,corpuslis):  # 计算单篇文章中各个词的TF-IDF,并返回字典
    outdic = {}
    tf = 0
    idf = 0
    dic = freqword(wordlis)
    for i in set(wordlis):
        #print(i)
        tf = dic[str(i)] / len(wordlis)  # 计算TF：某个词在文章中出现的次数/文章总词数
        #print(tf)
        # 计算IDF：log(语料库的文档总数/(包含该词的文档数+1))
        idf = math.log(len(corpuslis) / (wordinfilecount(str(i), corpuslis) + 1))
        #print(idf)
        tfidf = tf * idf  # 计算TF-IDF
        outdic[str(i)] = tfidf
    #orderdic = sorted(outdic.items(), key=operator.itemgetter(1), reverse=True)  # 按照键排序，降序
    #return orderdic
    return outdic
'''
def wordtoexcel(content): # 将word写入excel文件中,
    global sheet1
    for m in range(len(content)):
        sheet1.write(m + 1,0,str(content[m][0]))
        sheet1.write(m + 1,1, str(content[m][1]))

f = xlwt.Workbook()  # 创建工作簿
sheet1 = f.add_sheet('sheet1')
'''
def main():
    #excelway='C:\\Users\\lenovo\\Desktop\\陈育新\\python生成excel结果\\tfid.xls'
    corpuslis_wenti = exceltolist_wenti_tfidf.wenti_words
    corpuslis_wenzhang = exceltolist_wenzhang_tfidf.wenzhang_words
    corpuslis = corpuslis_wenti+corpuslis_wenzhang
    print(len(corpuslis))
    tfidf_word = []
    tfidf_corlis=[]
    for i in range(len(corpuslis)):
        tfidfdic = tf_idf(corpuslis[i], corpuslis) # 计算TF-IDF
        # print(tfidfdic)
        tfidf_word = tfidf_word + list(tfidfdic.keys())#查看全部单词
        tfidf_corlis.append(tfidfdic)#总数1127
    print("done!")
    #print(tfidf_word )
    #print(tfidf_corlis)
    return tfidf_word,tfidf_corlis

'''
    wordtoexcel(tfidfdic_all)
    f.save(excelway)
'''

#if __name__ == '__main__':

tfidf_word,tfidf_corlis=main()
