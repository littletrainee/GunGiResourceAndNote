# 可以將google 試算表所設定好的旗子各階段移動格數與方向圖的逗號分隔值檔轉換為markdown格式
import csv

a = []
b: list = []
c = ""
with open('c - c.csv', newline='')as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        a.append(row)

for i in a:
    for j in range(len(i)):
        if i[j] == '一':
            i[j] = '<span style="background-color: aqua;">　</span>'
        elif i[j] == '二':
            i[j] = '<span style="background-color: blue;">　</span>'
        elif i[j] == '三':
            i[j] = '<span style="background-color: green;">　</span>'
        elif i[j] == '紅':
            i[j] = '<span style="background-color: red;">　</span>'

        c = c + i[j] + "|"
    b += [c]
    c = ""


with open('output.md', 'w', newline='')as md:
    for t in b:
        md.write(t+'\n')
