import xlrd
import xlwt

'''
# 获取停用词
stopwords = []
file = open('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\stopwords_VSM.txt', 'r',encoding='utf-8')
for line in file:
    stopwords.append(line.strip())
file.close()

#去重重新写入excel
def exceltolist_clean(path,sheet):
    copy = []
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    for i in range(table.nrows):
        rows=[]
        rows_word_value=table.cell(i, 1).value
        if rows_word_value!='' and rows_word_value not in stopwords:
           for j in range(table.ncols):
               rows.append(table.cell(i, j).value)
        else:
            continue
        copy.append(rows)
    return copy

copy=exceltolist_clean('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\问题初始.xlsx','python_wenti')

#形成excel
f = xlwt.Workbook()  # 创建工作簿
sheets = f.add_sheet('sheet1')
for i in range(len(copy)):
    for j in range(len(copy[i])):
        sheets.write(i,j, str(copy[i][j]))
f.save('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\python_wenti_clean_VSM.xls')
print('数据录入完毕')


'''

#读取excel中某的文章编号及其对应单词/语义组，形成列表
def exceltolist(path,sheet,id):
    #number_word={}
    wenzhang_words=[]
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    for i in range(151):
        each_words = []
        for j in range(table.nrows):
            number = table.cell(j, 0).value
            word_semgroups = table.cell(j, id).value
            if int(number) == int(30798001+i):
               each_words.append(word_semgroups)
            else:
               continue
        #print(len(each_words),len(each_words))
        wenzhang_words.append(each_words)
        #number_word[str(i)] = each_words
    return wenzhang_words

#读取excel中某语义组及其对应单词，形成字典
def exceltodic(path,sheet):
    semgroup_words={}
    semgroup_list = ['activities & behaviors', 'anatomy', 'chemicals & drugs', 'devices', 'disorders', 'living beings', 'objects', 'phenomena', 'physiology', 'procedures']
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    for i in range(len(semgroup_list)):
        singlegroup_words=[]
        for j in range(table.nrows):
            semgroup = table.cell(j, 3).value
            word = table.cell(j, 2).value
            if semgroup == semgroup_list[i]:
               singlegroup_words.append(word)
            else:
               continue
        #print(len(singlegroup_words),len(singlegroup_words))
        semgroup_words[semgroup_list[i]]=singlegroup_words
        #number_word[str(i)] = each_words
    return semgroup_words

#计算文章中的唯一词（word_id),以字典形式保存
def word_id_(wenzhang_words):
    all_words=[]
    unique_words=[]
    word_id_={}
    for i in range(len(wenzhang_words)):
        for j in range(len(wenzhang_words[i])):
            all_words.append(wenzhang_words[i][j])
    unique_words=list(set(all_words))
    print(len(unique_words))
    for i in range(len(unique_words)):
        word_id_[str(unique_words[i])]=i
    return word_id_

#计算语义组-词概率矩阵
def P_t_s_(word_id,wenzhang_semgroup_words):
    P_t_s_=[]
    semgroup_list = ['activities & behaviors', 'anatomy', 'chemicals & drugs', 'devices', 'disorders', 'living beings',
                     'objects', 'phenomena', 'physiology', 'procedures']
    for i in range(len(semgroup_list)):
        semgroup=semgroup_list[i]
        p_singlegroup_word = []
        for j in word_id.keys():
            count = 0
            for word in wenzhang_semgroup_words[semgroup]:
                if j == word:
                   count+=1
                else:
                   continue
            p=count/len(wenzhang_semgroup_words[semgroup])
            p_singlegroup_word.append(p)
        sum_ = sum(p_singlegroup_word)
        print(sum_)
        P_t_s_.append(p_singlegroup_word)
    return P_t_s_

#计算文档-语义组概率矩阵
def P_s_d_(wenzhang_semgroups):
    semgroup_list = ['activities & behaviors', 'anatomy', 'chemicals & drugs', 'devices', 'disorders', 'living beings',
                     'objects', 'phenomena', 'physiology', 'procedures']
    P_s_d_=[]
    for i in range(len(wenzhang_semgroups)):
        p_singlewz_semgroup = []
        for j in range(len(semgroup_list)):
            semg=semgroup_list[j]
            count = 0
            for semgroup in wenzhang_semgroups[i]:
                if semgroup==semg:
                   count+=1
                else:
                   continue
            p=count/len(wenzhang_semgroups[i])
            p_singlewz_semgroup.append(p)
        sum_ = sum(p_singlewz_semgroup)
        print(sum_)
        P_s_d_.append(p_singlewz_semgroup)
    return P_s_d_

def writedoc_semToExcleFile(inputData,outPutFile):
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    for i in range(len(inputData)):
        for j in range(len(inputData[i])):
            sheet.write(i, j, str(inputData[i][j]))
    f.save(outPutFile)
    print('数据写入完毕!')

def writesem_wordToExcleFile(inputData,outPutFile):
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    for i in range(len(inputData)):
        for j in range(len(inputData[i])):
            sheet.write(j, i, str(inputData[i][j]))
    f.save(outPutFile)
    print('数据写入完毕!')

def index20_(word_id,P_t_s):
    index20=[]
    for i in range(len(P_t_s)):
        temp = []
        Inf = 0
        nums=P_t_s[i]
        for j in range(25):
            temp.append(nums.index(max(nums)))
            nums[nums.index(max(nums))] = Inf
        print(temp)
        index_word=[]
        for i in range(len(temp)):
            for word in word_id.keys():
                if temp[i]==word_id[word]:
                    index_word.append(word)
                else:
                    continue
        index20.append(index_word)
    #print(index20)
    return index20




def main():
    wenzhang_words = exceltolist('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\python_wenzhang_clean_VSM.xls','sheet1',2)
    #wenzhang_semgroups = exceltolist('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\python_wenzhang_clean.xls','sheet1', 3)
    #wenzhang_semgroup_words = exceltodic('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\python_wenzhang_clean.xls','sheet1')
    print(wenzhang_words)
    #print(wenzhang_semgroups)
    #print(wenzhang_semgroup_words)
    #word_id = word_id_(wenzhang_words)
    #print(word_id)
    #P_t_s=P_t_s_(word_id, wenzhang_semgroup_words)
    #for i in range(len(P_t_s)):
        #print(sum(P_t_s[i]))
    #P_s_d=P_s_d_(wenzhang_semgroups)
    #index20 = index20_(word_id, P_t_s)
    #writedoc_semToExcleFile(index20, 'C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\P_s_d(top25).xls')
    #writedoc_semToExcleFile(P_s_d, 'C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\P_s_d.xls')
    #writesem_wordToExcleFile(P_t_s, 'C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\P_t_s_2.xls')
    return wenzhang_words
    
wenzhang_words = main()

