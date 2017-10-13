import pymssql

conn = pymssql.connect(host='your mssql server ip', user='', password='', database='')
curs = conn.cursor()
sql = 'query ~'
curs.execute(sql)
rows = curs.fetchall() #data
desc = curs.description #colums name


for row in rows:
    columns = []
    for col in desc:
        columns.append(col[0])
    #print(dict(zip(columns, row)))
    dataDict = dict(zip(columns, row)) #  colums, row to dic


