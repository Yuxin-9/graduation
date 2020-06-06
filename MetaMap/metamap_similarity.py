import math
import xlwt
import exceltolist_wenti
import exceltolist_wenzhang

def freqword(word_id,wordlis_wenti): # 统计word_id(全文章所有词)中的各个词在一个问题中的频率，返回结果为字典，键为文章中的词，值为词对应的词频
  freword = {}
  sum=0
  for i in word_id.keys():
      count = 0
      for j in wordlis_wenti:
          if i==j:
              count+=1
          else:
              continue
      freword[str(i)]= count
      sum += count
  #print(freword)
  return freword,sum

def wordinfilecount(word_id, corpuslis_wenti):  # 查出包含单篇文章中的各个词对应的问题数，返回字典，键为文章中的各个词，值为包含该词的问题数
    word_in_corpwenti={}
    for word in word_id.keys():
        count = 0  # 计数器
        for wordlis in corpuslis_wenti:
            if word in set(wordlis):  # 只要问题出现该词，这计数器加1，所以这里用集合
                count = count + 1
            else:
                continue
        word_in_corpwenti[str(word)]=count
    #print(word,count)
    return word_in_corpwenti

def tf_idf(word_id,wordlis_wenti,corpuslis_wenti):  # 计算word_id在一个问题中各个词的TF-IDF,并返回字典
    outdic = {}
    tf = 0
    idf = 0
    sum_f = 0
    dic_word_f,sum= freqword(word_id,wordlis_wenti)
    dic_word_t= wordinfilecount(word_id, corpuslis_wenti)
    for i in word_id.keys():
        #print(i)
        if sum==0:        #len(wordlis_wenti)==0
           tf=0
        else:
           tf = dic_word_f[str(i)] / sum    #len(wordlis_wenti)  # 计算TF：某个词在问题中出现的次数/文章总词数 for word in dic_word_f.keys(): sum_f += int(dic_word_f[word])
        #print(tf)
        # 计算IDF：log(语料库的文档总数/(包含该词的文档数+1))
        if dic_word_t[str(i)]==0:
           idf=0
        else:
           idf = math.log(len(corpuslis_wenti) / dic_word_t[str(i)])
        #print(idf)
        tfidf = tf * idf  # 计算TF-IDF
        outdic[str(i)] = tfidf
    #orderdic = sorted(outdic.items(), key=operator.itemgetter(1), reverse=True)  # 按照键排序，降序
    #return orderdic
    return outdic

def p_wt(num_topics,word_id,topic_word):#计算word_id和所有主题的p_wt值，返回字典，键为word_id，值为词对应各个主题的P值（列表形式）
    #word_id=word_id  #调用lda形成的dictionary.token2id
    #topic_word=topic_word #调用lda形成的topic_word
    p_wt_dic={}
    for i in word_id.keys():
        pw_wt=[]
        _id = word_id[str(i)]
        for j in range(num_topics):
            p_wt=topic_word[j][int(_id)]
            pw_wt.append(p_wt)
        p_wt_dic[str(i)]=pw_wt
    return p_wt_dic

def f_tq(wordlis_wenti, corpuslis_wenti, num_topics, word_id, topic_word): #计算一个问题与所有主题的f_tq，返回字典，键为主题，值为f_tq
    tfidf_dic = tf_idf(word_id,wordlis_wenti,corpuslis_wenti)
    #print(tfidf_dic)
    p_wt_dic=p_wt(num_topics,word_id,topic_word)
    f_tq_dic={}
    for j in range(num_topics):
        f_tq=0
        for i in word_id.keys():
            sum_pwt=0
            p_wt_lis=p_wt_dic[str(i)]
            for n in range(len(p_wt_lis)):
                sum_pwt += p_wt_lis[n]
            if sum_pwt == 0:
                one_f_tq = 0
            else:
                one_f_tq=tfidf_dic[str(i)]*(p_wt_lis[j]/sum_pwt)
            f_tq += one_f_tq
        f_tq_dic[str(j)]=f_tq
    return f_tq_dic

def p_td(num_topics, corpuslis_wenzhang, doc_topic): #返回各个主题对应所有文档的p_td，键为主题，值为主题对应各个文档的p_td（列表形式）
    p_td_dic = {}
    for j in range(num_topics):
        pd_td=[]
        for k in range(len(corpuslis_wenzhang)):
            p_td = doc_topic[k][j]
            pd_td.append(p_td)
        p_td_dic[str(j)] = pd_td
    return p_td_dic

def m_dq(wordlis_wenti, corpuslis_wenti, corpuslis_wenzhang, num_topics, word_id, topic_word, doc_topic): #计算单个问题和151篇文章的m_dq，返回字典，键为文档号，值为文档与问题的m_dq值
    ftq = f_tq(wordlis_wenti, corpuslis_wenti, num_topics, word_id, topic_word)
    #print(ftq)
    p_td_dic = p_td(num_topics, corpuslis_wenzhang, doc_topic)
    #print(p_td_dic)
    m_dq_dic = {}
    for k in range(len(corpuslis_wenzhang)):
        m_dq = 0
        for j in range(num_topics):
            sum_mdq = 0
            p_td_lis=p_td_dic[str(j)]
            for n in range(len(p_td_lis)):
                sum_mdq += p_td_lis[n]
            if sum_mdq == 0:
               one_m_dq = 0
            else:
               one_m_dq = ftq[str(j)]*(p_td_lis[k]/sum_mdq)
            m_dq += one_m_dq
        m_dq_dic[str(k)] = m_dq
    return m_dq_dic

def writedoc_topicToExcleFile(inputData,outPutFile):#写入excel中
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    item_0 = inputData[0]
    i = 0
    for key in item_0.keys():#将其中一个字典中的键在excl中形成行，每个问题的文档数统一且对应
        sheet.write(0,i, key)
        i = i+1
    j = 1
    for item in inputData:#将开始填充各键对应的值，并换行
        k = 0
        for key in item:
            sheet.write(j,k, str(item[key]))
            k = k+1
        j = j+1#换行
    f.save(outPutFile)
    print('数据写入完毕!')

'''
wenti=exceltolist_wenti.wenti_words
wenzhang=exceltolist_wenzhang.wenzhang_words
word_id=exceltolist_wenzhang.word_id
doc_semgroups=exceltolist_wenzhang.P_s_d
semgroup_words=exceltolist_wenzhang.P_t_s
num_topics=10
similarity_list=[]
for i in range(len(wenti)):
    m=m_dq(wenti[i], wenti, wenzhang, num_topics, word_id, semgroup_words, doc_semgroups)
    similarity_list.append(m)
print(similarity_list)
writedoc_topicToExcleFile(similarity_list,'C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\similarity.xls')
print('OK!')
'''
def main():
    wenti = exceltolist_wenti.wenti_words
    wenzhang = exceltolist_wenzhang.wenzhang_words
    word_id = exceltolist_wenzhang.word_id
    doc_semgroups = exceltolist_wenzhang.P_s_d
    semgroup_words = exceltolist_wenzhang.P_t_s
    num_topics = 10
    ftq_list = []
    for i in range(len(wenti)):
        f=[]
        t = f_tq(wenti[i], wenti, num_topics, word_id, semgroup_words)
        for j in t.keys():
            f.append(t[j])
        ftq_list.append(f)
    print(len(ftq_list), len(ftq_list[0]))
    return ftq_list

ftq_list=main()







