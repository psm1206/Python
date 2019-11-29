#oracle_test_module.py
#코드출처 : https://oracle.github.io/python-cx_Oracle/
import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
db = cx_Oracle.connect("kosa", "0000", dsn)
cursor = db.cursor()
cursor.execute("""SELECT * FROM emp""")
row = cursor.fetchone()
print(row)
