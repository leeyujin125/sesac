import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='ShopDB',
                       charset='utf8')

cur = conn.cursor()

sql = "INSERT INTO Product(Pcode, pName, price, amount) VALUES('p0007', '핸드폰', 800000, 5)"
cur.execute(sql)

#영구 반영 => DB에 반영
conn.commit()

conn.close()