import math
import xlwt
import tfidf_math12

#文章问题关键词合并
def CreateVocabulary(tfidf_all):
    vocabulary=[]
    for i in range(len(tfidf_all)):
        if tfidf_all[i] not in vocabulary:
           vocabulary.append(tfidf_all[i])
    return vocabulary

#将每个问题/文章的向量维数统一,词顺也统一，已含的值为tfidf，不包含则为0
def union_dict(dicvoc,dic):
    _total=dicvoc
    for i in dic:
        _total[str(i)] = dic[i]
        '''
        j = 0
        while j < len(dicvoc):
            if _total[i] == dicvoc[j]:
                _total[j] = dic[i][1]
                break
            else:
                j = j + 1
        '''
    return _total

def ComputeVector(dic=None,vocabulary=None):
    dicVector = {}
    for elem in vocabulary:
        dicVector[elem]=0
    # dicVector = sorted(dicVector.iteritems(),key= lambda asd:asd[1], reverse=True)
    dicTemp=union_dict(dicVector,dic);
    # dicTemp = sorted(dicTemp.iteritems(),key= lambda asd:asd[1], reverse=True)
    return  dicTemp

#计算每个问题与151篇文章的相似度,
def ComputeSimlirity(WentiVector=None,WenzhangVector=None):
    x=0.0
    y1=0.0
    y2=0.0
    for k in WentiVector:# because of the element of dic1 and dic2 are the same
        temp1=float(WentiVector[k])
        temp2=float(WenzhangVector[k])
        x=x+ (temp1*temp2)
        y1+=pow(temp1,2)
        y2+=pow(temp2,2)
    return x/math.sqrt(y1*y2)
'''
def Simliritytoexcel(Simlirityall_value=None):
    global sheet
    for i in range(len(Simlirityall_value)):
        for j in range(len(Simlirityall_value[i])):
            sheet.write(i,j, str(Simlirityall_value[i][j]))
'''
def main():
    word_tfidf = tfidf_math12.tfidf_word
    corlis_tfidf = tfidf_math12.tfidf_corlis
    Vocabulary_all=CreateVocabulary(word_tfidf)
    Vector_all=[]
    Vector_wenti=[]
    Vector_wenzhang=[]
    Simlirity_all=[]
    for i in range(len(corlis_tfidf)):
        Vector_all.append(ComputeVector(corlis_tfidf[i],Vocabulary_all))
    Vector_wenti=Vector_all[0:976]
    #print(Vector_all[0:3])
    Vector_wenzhang=Vector_all[976:]
    for i in range(len(Vector_wenti)):
        Simlirity_wenti = []
        for j in range(len(Vector_wenzhang)):
            Simlirity_wenti.append(str(ComputeSimlirity(Vector_wenti[i],Vector_wenzhang[j])))
        Simlirity_all.append(Simlirity_wenti)#相似度值无序,文章序号有序
        #Simlirity_all[str(i + 1)]=sorted(Simlirity_wenti, reverse=True)#取阈值修改处
    print(len(Simlirity_all))
    return Simlirity_all


if __name__ == '__main__':
    Simlirityall=main()
    f = xlwt.Workbook()  # 创建工作簿
    sheets = f.add_sheet('Sheet1')
    for i in range(len(Simlirityall)):
        for j in range(len(Simlirityall[i])):
            sheets.write(i, j, str(Simlirityall[i][j]))
    f.save('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\similarity_VAM(1).xls')
    #Simliritytoexcel(Simlirityall)
    #f.save(excelway)
    print('数据录入完毕')
