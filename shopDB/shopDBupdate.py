import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='ShopDB',
                       charset='utf8')

cur = conn.cursor()

updateSql = "UPDATE Product SET price = 50000 where pCode = 'p0003'"

cur.execute(updateSql)

conn.commit()

conn.close()