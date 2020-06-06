#将其保存到excel中，形成文件
import xlwt

#将文档与主题概率格式改变
def saveAticleTopicsResultToFile(result):
    r = []
    i = 1
    for article in result:
        item = {'article_id/topicType':i}#每一次大循环，形成一个新字典项
        for topic_result in article:
            item[str(topic_result[0])] = topic_result[1]
        r.append(item)#把每个item(字典）加入到r(列表）
        i += 1
    #print(r)
    return r

'''
inputData: 列表，含有多个字典;例如：[{'key_a':'123'},{'key_b':'456'}]
outPutFile：输出文件名，例如：'data.xlsx'
'''
def writedoc_topicToExcleFile(inputData,outPutFile):
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    item_0 = inputData[0]
    i = 0
    for key in item_0.keys():#将其中一个字典中的键在excl中形成行，每个文档主题数统一且对应
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

#将主题与词概率分布写入excel
def writetopic_wordToExcleFile(inputData,outPutFile):
    f = xlwt.Workbook()  # 创建工作簿
    sheet = f.add_sheet('Sheet1')
    for i in range(len(inputData)):
        sheet.write(i,0, inputData[i][0])
        sheet.write(i,1, inputData[i][1])
    f.save(outPutFile)
    print('数据写入完毕!')
'''
doc=[[(0, 0.043816663), (1, 0.04390042), (2, 0.91228294)], [(0, 0.03811829), (1, 0.03805999), (2, 0.9238217)]]
a=saveAticleTopicsResultToFile(doc)
writeDataToExcleFile(a,'C:\\Users\\asus\\Documents\\testing\\6.xlsx')
'''