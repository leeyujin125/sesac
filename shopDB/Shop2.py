import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='ShopDB',
                       charset='utf8')

cur = conn.cursor()

# SQL문에 변수 사용 (execute() 함수에 매개변수 전달 -> 매개변수는 튜플(tuple) 형식으로 전달됨)

# sql = "SELECT * FROM Product WHERE pCode = %s"
# cur.execute(sql, ('p0002'))

# result = cur.fetchone()
# print(result)


# # 가격이 50 ~ 100만원 사이의 제품을 검색
# sql = "SELECT * FROM Product WHERE price BETWEEN 500000 AND 1000000"
# cur.execute(sql)

# result = cur.fetchall()
# print(result)


# 가격이 10만원 미만인 제품들의 평균가와 수량의 합을 계산
sql = "SELECT avg(price), sum(amount) FROM Product WHERE price < 100000"
cur.execute(sql)

result = cur.fetchall()
print(result)

conn.close()