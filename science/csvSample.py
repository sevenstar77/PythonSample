import codecs

file_name = "test1.csv"
listData = []


csv = codecs.open(file_name, "r", "utf-8").read()
print("csv", csv)
rows = csv.split('\n')

for row in rows:
    if rows == "":
        continue
    cells = row.split(",")
    listData.append(cells)

print(listData)

for c in listData:
    print(c[1], c[2], c[3])