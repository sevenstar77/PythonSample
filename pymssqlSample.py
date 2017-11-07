import pymssql

conn = pymssql.connect(host='your mssql server ip', user='', password='', database='')
def executeQuery(query):
    curs = conn.cursor()
    sql = 'query ~'
    curs.execute(sql)

    rows = curs.fetchall() #data
    desc = curs.description #colums name

    result = []
    for row in rows:
        columns = []
        for col in desc:
            columns.append(col[0])
        #print(dict(zip(columns, row)))
        dataDict = dict(zip(columns, row)) #  colums, row to dic
        for key, val in dataDict.items():
            if str(type(val)) == "<class 'decimal.Decimal'>":
                dataDict[key] = float(val)
            if str(type(val)) == "<class 'datetime.datetime'>":
                dataDict[key] = str(val)
        result.append(dataDict)
    return result

def updateQuery(query):

    with conn.cursor() as cursor:
        cursor.exeucte(query)
        conn.commit()


#commit / rollback
isSuccess = True
conn = pymssql.connect(host='your mssql server ip', user='', password='', database='')
cur = conn.cursor()
cur.execute('create table reservation(reservationNum text, name text);')
if isSuccess == True:
    conn.commit()
else:
    conn.rollback()