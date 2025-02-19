import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', 
                                 port=3306, user='root', 
                                 password='root', 
                                 database='rishika_db', 
                                 charset='utf8')
    print('Database connected')
    return connection

def disconnect_db(connection):
    connection.close()
    print('Database disconnected')

connection = connect_db()
disconnect_db(connection)