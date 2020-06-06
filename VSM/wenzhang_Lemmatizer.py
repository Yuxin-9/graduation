import os
import re
import xlwt
import jieba
from nltk.stem import WordNetLemmatizer
from nltk.tag import StanfordPOSTagger

modelfilename='C:\\Users\\asus\\AppData\\Roaming\\nltk_data\\stanfordpostagger\\models\\english-bidirectional-distsim.tagger'
pathtojar='C:\\Users\\asus\\AppData\\Roaming\\nltk_data\\stanfordpostagger\\stanford-postagger.jar'
eng_tagger = StanfordPOSTagger(model_filename=modelfilename,path_to_jar=pathtojar)
lemmatizer=WordNetLemmatizer()
'''
#将文件路径全部放入filepaths中
list = os.listdir(rootdir)
filepaths = []
for i in range(len(list)):#151
    path = os.path.join(rootdir,list[i])
    if os.path.isfile(path):
       filepaths.append(path)
'''
#将文件按照顺序排列 【1,2,3】
rootdir = 'C:\\Users\\asus\\Desktop\\测试\\测试文章'
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

# 读取同义词表：并生成一个字典。
combine_dict = {}
for line in open("C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\同义词替换_文章.txt", "r"):
    seperate_word = line.strip().split(' ')
    for i in range(1, len(seperate_word)):
        combine_dict[seperate_word[i]] = seperate_word[0]
#print(combine_dict)

#去掉数字/切词/词形还原/合并部分单词的同义词
col1=[]
col3=[]
for i in range (len(docs)):
    col1 = re.sub(r'[^\x00-\x7f]', ' ', docs[i])
    col1 = ' '.join(jieba.cut(re.sub(r'\d+', ' ', col1))).split(' ')
    col2 = []
    for word,tag in eng_tagger.tag(col1):
        wntag = tag[0].lower()
        wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
        if not wntag:
           lemma = word.lower()
        else:
           lemma = lemmatizer.lemmatize(word.lower(), wntag)
        if lemma in combine_dict:
           word_hebing = combine_dict[lemma]
        else:
           word_hebing=lemma
        col2.append(word_hebing)
    col3.append(col2)
print(len(col3))

# 获取停用词
stopwords = []
file = open('D:\\python project\\stopword_english.txt', 'r',encoding='utf-8')
for line in file:
    stopwords.append(line.strip())
file.close()

#去除停用词
texts2 = []
for i in range(len(col3)):
    texts1 = []
    for j in col3[i]:
        if j!='' and j not in stopwords:
           texts1.append(j)
    #print(len(texts1))
    texts2.append(texts1)
print('done!')
'''
#将所得词写入excel中
texts3=[]
for i in range(len(texts2)):
    for j in range(len(texts2[i])):
        texts3.append(texts2[i][j])
print(len(texts3))
print(len(set(texts3)))

f = xlwt.Workbook()  # 创建工作簿
sheets = f.add_sheet('sheet1')
for n in range(len(texts3)):
    sheets.write(n, 0, str(texts3[n]))
f.save('C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\VSM\\wenzhang_words.xls')
print('数据录入完毕')
'''