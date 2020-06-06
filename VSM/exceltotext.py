
'''
import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\lenovo\\Desktop\\陈育新\\hypertension相关评价\\hypertension总问题集 - 副本.xlsx')
#textfile=open('C:\\Users\\asus\\Desktop\\hypertension相关评价\\hypertension总问题集.txt','w',encoding='utf-8')
sheet = wb.get_sheet_by_name('sheet1')
col = list()
# 创建一个大小为976的list，python中list相当于数组
i=0
for cellObj in  sheet['B']:
    col.append(cellObj.value)
    i=i+1
col.remove(col[0])
'''
#读取excel中某一列的数据，形成列表
import xlrd

def exceltolist(path,sheet,col):
    col_values=[]
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    col_values = table.col_values(col)
    #print(len(col_values))
    return col_values

