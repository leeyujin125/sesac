import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='ShopDB',
                       charset='utf8')

cur = conn.cursor()

deleteSql = "DELETE FROM Product WHERE pCode = 'p0007'"
cur.execute(deleteSql)

conn.commit()

conn.close()