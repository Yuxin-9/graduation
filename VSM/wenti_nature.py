#将976个问题切词,最原始结果
import os
import re
import xlwt
import xlrd
import jieba
import numpy as np
#from nltk.stem import WordNetLemmatizer
#from nltk.tag import StanfordPOSTagger

#读取excel中某一列的数据，形成列表
def exceltolist(path,sheet,col):
    col_values=[]
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    col_values = table.col_values(col)
    #print(len(col_values))
    return col_values

ques=exceltolist('C:\\Users\\asus\\Desktop\\hypertension相关评价\\hypertension总问题集.xlsx','Sheet2',0)
#print(ques)
'''
# 读取同义词表：并生成一个字典。
combine_dict = {}
for line in open("C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\同义词替换_问题.txt", "r"):
    seperate_word = line.strip().split(' ')
    for i in range(1, len(seperate_word)):
        combine_dict[seperate_word[i]] = seperate_word[0]
#print(combine_dict)
'''
#去掉数字/切词
col1=[]
col2=[]
for i in range (len(ques)):
    col1 = re.sub(r'[^\x00-\x7f]', ' ', ques[i])
    col1=' '.join(jieba.cut(re.sub(r'\d+', ' ', col1))).split(' ')
    col2.append(col1)
print(len(col2))
'''
# 获取停用词
stopwords = []
file = open('D:\\python project\\stopword_english.txt', 'r',encoding='utf-8')
for line in file:
    stopwords.append(line.strip())
file.close()
'''
col3=[]
for i in range(len(col2)):
    col3.append(len(col2[i]))
average = np.mean(col3)
a=np.std(col3, ddof = 1)
b=300165/976
print(average,a,b)
#将所得词写入excel中
texts=[]
for i in range(len(col2)):
    for j in range(len(col2[i])):
        texts.append(col2[i][j])
print(len(texts))
print(len(set(texts)))

