import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', 
                                 port=3306, user='root', 
                                 password='root', 
                                 database='rishika_db', 
                                 charset='utf8')
        print('Database connected')
        return connection
    except:
        print('Database connection failed')
            
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('Database disconnected')
    except:
        print('Error while disconnecting Database')   

def create_db():
    connection = connect_db()
    query = 'create database IF NOT EXISTS rishika_db;'
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    disconnect_db(connection)

def insert_row():
    connection = connect_db()

create_db()
insert_row()      