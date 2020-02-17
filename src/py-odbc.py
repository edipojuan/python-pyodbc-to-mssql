import pyodbc
from settings import SERVER, DATABASE, LOGIN, PASSWORD

str = 'DRIVER={ODBC Driver 17 for SQL Server}'
str += ';SERVER=' + SERVER + ';DATABASE=' + DATABASE
str += ';UID=' + LOGIN + ';PWD=' + PASSWORD

conn = pyodbc.connect(str)

cursor = conn.cursor()

cursor.execute('SELECT "Édipo Juan" AS Name, 31 AS YearsOld')
row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()
