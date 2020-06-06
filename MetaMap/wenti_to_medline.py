import xlrd
import re
#读取excel中某一列的数据，形成列表

def exceltolist(path,sheet,col):
    col_values=[]
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    col_values = table.col_values(col)
    #print(len(col_values))
    return col_values

def list_to_medline(wenti,path):
    file_med = open(path, mode='w',encoding='utf-8')
    n=30798001
    for i in range(len(wenti)):
        wen_ti=re.sub(r'[^\x00-\x7f]', ' ', wenti[i].replace('\n',' '))
        file_med.write('PMID- '+str(n)+'\n'+'OWN - NLM\n'+'TI  - hypertension\n'+'AB  - '+str(wen_ti)+'\n\n')
        n += 1
    file_med.close()

wenti=exceltolist('C:\\Users\\asus\\Desktop\\hypertension相关评价\\hypertension总问题集.xlsx','Sheet2',0)
print(len(wenti))
path='C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\wenti_to_medline.txt'
list_to_medline(wenti,path)
