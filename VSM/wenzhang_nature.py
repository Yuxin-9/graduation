import os
import re
import xlwt
import jieba
import numpy as np

#将文件按照顺序排列
rootdir = 'C:\\Users\\asus\\Desktop\\hypertension相关评价\\推荐文章text'
filelists = os.listdir(rootdir)
sort_num_first = []
for file in filelists:
    sort_num_first.append(int(file.split(".")[0]))  # 根据分割，转化为数字类型
    sort_num_first.sort()
sorted_file = []
for sort_num in sort_num_first:
    for file in filelists:
        path = os.path.join(rootdir, file)
        if  str(sort_num) == file.split(".")[0] and os.path.isfile(path):
            sorted_file .append(path)
#print(sorted_file)
docs = [open(f, 'r').read() for f in sorted_file]
'''
# 读取同义词表：并生成一个字典。
combine_dict = {}
for line in open("C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\同义词替换_文章.txt", "r"):
    seperate_word = line.strip().split(' ')
    for i in range(1, len(seperate_word)):
        combine_dict[seperate_word[i]] = seperate_word[0]
#print(combine_dict)
'''
#去掉数字/切词
col1=[]
col2=[]
for i in range (len(docs)):
    col1 = re.sub(r'[^\x00-\x7f]', ' ', docs[i])
    col1=' '.join(jieba.cut(re.sub(r'\d+', ' ', col1))).split(' ')
    col2.append(col1)
print(len(col2))

col3=[]
for i in range(len(col2)):
    col3.append(len(col2[i]))
average = np.mean(col3)
a=np.std(col3, ddof = 1)
print(average,a)

d=[1,2,3]
d=np.std(d, ddof = 1)
print(d)


#将所得词写入excel中
texts=[]
for i in range(len(col2)):
    for j in range(len(col2[i])):
        texts.append(col2[i][j])
print(len(texts))
print(len(set(texts)))