import sqlalchemy

def connect(user, password, db, host='localhost', port=5432):
    print('connect~')
    host = '127.0.0.1'
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    conn = sqlalchemy.create_engine(url, client_encoding='utf-8')
    meta = sqlalchemy.MetaData(bind=conn, reflect=True)

    return conn, meta