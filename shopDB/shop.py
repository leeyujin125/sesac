import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='ShopDB',
                       charset='utf8')

# 커서 생성하기 => 커서 = 연결자.cursor()

cur = conn.cursor() #일반적으로 커서는 cur이라고 만이들 쓴다.

selectAll = "SELECT * FROM Product;"
cur.execute(selectAll)

result = cur.fetchone()
print("데이터 출력: ", result)

result = cur.fetchall()
print("데이터 출력: ", result)

# result = cur.fetchmany(2)

result = cur.fetchone()
print("데이터 출력: ", result) #위에 fetchall에서 저장된 데이터를 전부 출력했기 때문에 None이 나옴.

# for data in result:
#   print(data)

conn.close()