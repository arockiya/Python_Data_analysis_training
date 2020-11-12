DB_HOST = "192.168.0.107"
DB_NAME = "AdventureWorks"
DB_USER = "pi"
DB_PASS = "Selva@91"

import psycopg2
import pandas as pd

conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER, password=DB_PASS,host=DB_HOST)
print("Connection Established")

cur=conn.cursor()

cur.execute("select * from sales.salesorderheader;")

df = pd.DataFrame(cur.fetchall())
print(df.describe(include='all'))

conn.close()