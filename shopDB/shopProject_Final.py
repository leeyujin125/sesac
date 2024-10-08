import pymysql
from prettytable import PrettyTable
from termcolor import colored

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='ShopDB',
                       charset='utf8')

cur = conn.cursor()

print(colored("🌱 제품 관리 프로그램 🌱", 'green'))

while True:
    print(colored("\n===== 메뉴 =====", 'cyan'))
    print(colored("1. 전체 제품보기", 'yellow'))
    print(colored("2. 제품 검색", 'yellow'))
    print(colored("3. 제품 추가", 'yellow'))
    print(colored("4. 제품 수정", 'yellow'))
    print(colored("5. 제품 삭제", 'yellow'))
    print(colored("6. 종료", 'red'))
    menu = int(input("메뉴를 선택하세요: "))

    if menu == 1:  # 전체 출력
        selectAll = "SELECT * FROM Product;"
        cur.execute(selectAll)
        results = cur.fetchall()
        
        table = PrettyTable(['제품번호', '제품명', '가격', '수량'])
        for row in results:
            table.add_row(row)
        print(colored(table, 'cyan'))

    elif menu == 2:  # 검색
        searchInput = input("제품 번호를 입력하세요: ")
        searchProduct = "SELECT * FROM Product WHERE pCode = %s"
        cur.execute(searchProduct, (searchInput,))
        results = cur.fetchall()
        
        if results:
            table = PrettyTable(['제품번호', '제품명', '가격', '수량'])
            for row in results:
                table.add_row(row)
            print(colored(table, 'cyan'))
        else:
            print(colored("⚠️ 해당 제품이 없습니다. ⚠️", 'red'))

    elif menu == 3:  # 추가
        print(colored("추가하실 제품의 정보를 입력해주세요.", 'cyan'))
        insertPcode = input("제품번호: ")
        insertpName = input("제품명: ")
        insertPrice = int(input("가격: "))
        insertAmount = int(input("수량: "))
        
        insertProduct = "INSERT INTO Product(Pcode, pName, price, amount) VALUES (%s, %s, %s, %s)"
        cur.execute(insertProduct, (insertPcode, insertpName, insertPrice, insertAmount))
        conn.commit()
        print(colored("제품 추가 완료.", 'green'))

    elif menu == 4:  # 수정
        update = input("수정하실 제품번호를 입력하세요: ")
        while True:
            print(colored("어떤 사항을 수정하시겠습니까?", 'cyan'))
            print("1. 제품명  2. 가격  3. 수량")
            whichUpdate = int(input("(제품번호는 수정할 수 없습니다.): "))
            
            if whichUpdate == 1:
                updatePname = input("새롭게 수정하실 제품명을 입력하세요: ")
                updatepName = "UPDATE Product SET pName = %s WHERE Pcode = %s"
                cur.execute(updatepName, (updatePname, update))
                conn.commit()
                print(colored("제품명 수정 완료.", 'green'))
                break
            elif whichUpdate == 2:
                updatePrice = int(input("새롭게 수정하실 가격을 입력하세요: "))
                update_price = "UPDATE Product SET price = %s WHERE Pcode = %s"
                cur.execute(update_price, (updatePrice, update))
                conn.commit()
                print(colored("가격 수정 완료.", 'green'))
                break
            elif whichUpdate == 3:
                updateAmount = int(input("새롭게 수정하실 수량을 적어주세요: "))
                update_amount = "UPDATE Product SET amount = %s WHERE Pcode = %s"
                cur.execute(update_amount, (updateAmount, update))
                conn.commit()
                print(colored("수량 수정 완료.", 'green'))
                break
            else:
                print(colored("⚠️ 수정할 수 없는 사항이거나 없는 정보입니다. ⚠️", 'red'))

    elif menu == 5:  # 삭제
        deleteProduct = input("삭제하실 제품번호를 입력하세요: ")
        delete_product = "DELETE FROM Product WHERE pCode = %s"
        cur.execute(delete_product, (deleteProduct,))
        conn.commit()
        print(colored("제품 삭제 완료.", 'green'))

    elif menu == 6:
        print(colored("🌱 프로그램 종료 🌱", 'green'))
        conn.close()
        break

    else:
        print(colored("⚠️ 지원하지 않는 메뉴입니다. ⚠️", 'red'))
