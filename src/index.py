import pyodbc

server = '...'
database = '...'
username = '...'
password = '...'

driver = 'DRIVER={ODBC Driver 17 for SQL Server}'

str = driver + ';SERVER=' + server + ';DATABASE=' + \
    database + ';UID=' + username + ';PWD=' + password

conn = pyodbc.connect(str)

cursor = conn.cursor()

cursor.execute('select top 10 * from Usuario')
row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()
