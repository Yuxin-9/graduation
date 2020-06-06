import os
import LDA_similarity2

resultWriter = open("C:\\Users\\asus\\Desktop\\hypertension相关评价\\cytoscape网络图\\主题ftq.txt", "w")
ftq=[]
ftq=LDA_similarity2.ftq_list
for i in range(len(ftq)):
    for j in range(len(ftq[i])):
        resultWriter.write("问题" + str(i+1) + "\t" + "主题" +str(j+1)+ "\t"+str(ftq[i][j])+"\n")
resultWriter.close()
print("ok")