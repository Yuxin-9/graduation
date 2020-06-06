import os
import metamap_similarity

resultWriter = open("C:\\Users\\asus\\Desktop\\hypertension相关评价\\cytoscape网络图\\语义组ftq.txt", "w")
ftq=[]
ftq=metamap_similarity.ftq_list
for i in range(len(ftq)):
    for j in range(len(ftq[i])):
        resultWriter.write("问题" + str(i) + "\t" + "主题" +str(j)+ "\t"+str(ftq[i][j])+"\n")
resultWriter.close()
print("ok")