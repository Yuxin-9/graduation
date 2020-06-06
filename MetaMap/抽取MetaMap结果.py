# python3.6
# for abstract medmap result,must add a new line to
# end of file and write Processing
import re, os

textReader = open("C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\metamap\\wenzhang122.out.txt")
resultWriter = open("C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\metamap\\result_wenzhang.txt", "w")

text = textReader.read()

regex = re.compile(r"(g \d+.ab.\d+)(.*?)Processin", re.DOTALL)
regex2 = re.compile(r">>>>> Mappings(.*?)<<<<< Mappings", re.DOTALL)
regex3 = re.compile(r" +\d+ +(.*?\[.*?\])", re.DOTALL)
# 这一步得到process编号和改变编号所有其余
step1 = regex.findall(text)

for i in step1:
    print(i[0])
    # 这一步分离包括phrase与>>>>>mapping的文本，得到同一个process下的多个mapping
    step2 = regex2.findall(i[1])
    for j in step2:
        # 接下来两步分离一个>>>>>>mapping中所有的Meta Mapping，并取得第一个
        temp = j.split("Meta Mapping")
        string = temp[1]#len(temp) - 1
        string = regex3.findall(string)
        for k in string:
            resultWriter.write("Processin" + i[0] + "\t" + k + "\n")
resultWriter.close()
