import xlrd

#读取excel中某的问题编号及其对应单词，形成列表
def exceltolist(path,sheet,id):
    #number_word={}
    wenti_words=[]
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    for i in range(976):
        each_words = []
        for j in range(table.nrows):
            number = table.cell(j, 0).value
            word = table.cell(j, id).value
            if int(number) == int(30798001+i):
               each_words.append(word)
            else:
               continue
        #print(len(each_words))
        wenti_words.append(each_words)
    return wenti_words
def main():
    wenti_words = exceltolist('C:\\Users\\asus\\Desktop\\新建文件夹\\初评价\\MetaMap\\整理\\python_wenti_clean.xls','sheet1',2)
    #print(wenti_words)
    return wenti_words


wenti_words=main()
