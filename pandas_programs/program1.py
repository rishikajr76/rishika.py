import pandas as pd

def read_excel_file():
    file_path = './students.xlsx'

    df = pd.read_excel(file_path)

    print(df.count())
    print(df.head())
    print(df.tail())

def read_excel_file1():
    file_path = './students.xlsx'
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        print(row[0], '  ', row[1])

def read_excel_file2():
    file_path = './students.xlsx'
    df = pd.read_excel(file_path)
    for row in df.iterrows():
       print(row[1][0], row[1][1])