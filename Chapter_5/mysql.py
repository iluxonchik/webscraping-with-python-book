import pymysql
import connectvars

conn = pymysql.connect(host=connectvars.DB_HOST, user=connectvars.DB_USER, passwd=connectvars.DB_PWD, db="mysql")
cur = conn.cursor()

cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()