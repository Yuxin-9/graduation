import os
import re
import xlrd
import xlwt

def exceltolist(path,sheet,col):
    col_values=[]
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    col_values = table.col_values(col)
    #print(len(col_values))
    return col_values

def list_to_medline(wenzhang,path):
    file_med = open(path, mode='w')
    n=30798001
    for i in range(len(wenzhang)):
        file_med.write('PMID- '+str(n)+'\n'+'OWN - NLM\n'+'TI  - hypertension\n'+'AB  - '+str(wenzhang[i])+'\n\n')
        n += 1
    file_med.close()

def writelistToExcleFile(inputData,outPutFile):
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    for i in range(len(inputData)):
        wenzhang = re.sub(r'[^\x00-\x7f]', ' ', inputData[i])
        sheet.write(i,0, wenzhang.replace('\n',' '))
    f.save(outPutFile)
    print('数据写入完毕!')

rootdir = 'C:\\Users\\asus\\Desktop\\hypertension相关评价\\推荐文章text - 副本'
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
wenzhang = [open(f, 'r').read() for f in sorted_file]
print(len(wenzhang))
outPutFile='C:\\Users\\asus\\Desktop\\hypertension相关评价\\推荐文章_副本.xls'
writelistToExcleFile(wenzhang,outPutFile)

wenzhang=exceltolist('C:\\Users\\asus\\Desktop\\hypertension相关评价\\推荐文章_副本.xls','Sheet1',0)
print(len(wenzhang))
path='C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\122文章\\wenzhang_to_medline.txt'
list_to_medline(wenzhang,path)
