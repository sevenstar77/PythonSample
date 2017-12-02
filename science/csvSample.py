import codecs

file_name = "test1.csv"
listData = []


csv = codecs.open(file_name, "r", "utf-8").read()
#print("csv", csv)
rows = csv.split('\n')
#print("rows", rows)
for row in rows:
    print('row~~', row)
    if rows == "":
        continue
    cells = row.split(",")
    print('celles', cells)
    listData.append(cells)

#print(listData)

#for c in listData:
#    print(c[1], c[2], c[3])