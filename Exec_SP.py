import pyodbc

def read(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute("exec Usp_ConfigRead")
    for row in cursor:
        print(f'row = {row}')
    print()

conn= pyodbc.connect(
    "Driver={SQL Server};"
    "server=dbswd0094;"
    "Database=CS_IM;"
    "Trusted_Connection=yes;"
)

read(conn)
conn.close()
