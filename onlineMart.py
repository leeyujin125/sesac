#변수, 연산, 함수, 제어문 활용하여 응용

#간단한 마트 프로그램
#상품 이름, 가격, 재고, 상품 코드

#상품 코드 = 특정 상품만 할인 적용
#상품 검색 = 이름으로
#재고 없으면 '재고 없음' 출력
#메뉴 만들기

#변수 productName, productPrice, productInventory(재고), productCode(상품코드)

products =[ #products라는 이름의 리스트 생성. 이 리스트는 딕셔너리 구조를 가지고 있음.
           #name이라는 이름의 키(key)와 딸기라는 이름의 값(value) 이하 생략.. 들이 쌍으로 구성되어있음
      {"name": "딸기", "price" : 5000, "inventory": 10, "code": hash(1)},
      {"name": "수박", "price" : 4000, "inventory": 8, "code": hash(2)},
      {"name": "참외", "price" : 2500, "inventory": 15, "code": hash(3)},
      {"name": "공구", "price" : 3500, "inventory": 3, "code": hash(4)},
      {"name": "노트", "price" : 1000, "inventory": 30, "code": hash(5)},
      {"name": "핸드폰 케이스", "price" : 7000, "inventory": 0, "code": hash(6)}
]

def print_product(product): #print_product라는 이름의 함수 선언, 필수 매개변수 product
  print(f"상품명: {product['name']}, 가격: {product['price']}, 재고: {product['inventory']}")
  #이 함수를 호출하였을 때 상품명과 가격 등등이 출력될 수 있도록 f-string을 이용하여 구문 작성

while True: #메뉴를 보여주기 위한 반복문 실행
  print("🏪온라인 마트🏪")
  print("1. 상품 검색")
  print("2. 상품 전체 보기")
  print("3. 할인 상품 보기")
  print("4. 쇼핑 끝내기")
  menu = int(input("원하시는 메뉴 번호를 입력하세요: ")) #메뉴의 번호를 정수로 변환하면서 입력받고 menu 변수에 저장

  if menu == 1: #위에서 입력받은 메뉴가 1이라면
    search_productName = input("상품의 이름을 입력하세요: ") #사용자가 검색할 상품의 이름을 입력받는다 -> search.. 변수에 저장
    found = False #상품을 찾았는지를 확인하기 위한 불리언 변수 found를 선언하고 False 값을 대입
    for product in products: #리스트 products에 product를 대입하여 반복문 실행
      if product['name'] == search_productName: #만약 위에서 입력받은 상품명이 product(=products) 리스트에 있는 이름과 같다면
        found = True #found 변수의 값을 True로 바꿈
        if product['inventory'] == 0: #만약 입력받은 제품의 재고가 0이라면
          print(f"{search_productName}의 상품 재고가 모두 소진되었습니다.") #재고 없음에 대한 문구 출력
        else: #재고가 있다면
          print_product(product) #상품 정보를 출력하기 위한 print_product 함수 호출, 리스트 호출을 위한 product를 매개변수로 사용.
        break #반복문 종료
    if not found: #만약 입력받은 상품명이 존재하지 않다면
      print(f"{search_productName}의 상품이 존재하지 않습니다.") #상품이 없다는 문구 출력

  elif menu == 2: #위에서 입력받은 메뉴가 2라면
    print("\n전체 상품")
    for product in products: #리스트 products에 product를 대입하여 반복문 실행
        print_product(product) #전체 상품 출력을 위해 print_product를 호출. 리스트 출력을 위해 product를 매개변수로 사용

  elif menu == 3: #위에서 입력받은 메뉴가 3이라면
    print("할인하는 상품 입니다.")
    for product in products: #products 리스트에 product를 대입하여 반복문 실행
      if product['code'] % 2 == 0: #만약 product 리스트(=products)의 해시 코드를 2로 나누어서 나머지가 0이라면
        discounted_price = product['price'] * 0.9 #discounted_price라는 이름의 변수에 가격 키값을 10% 할인한 가격을 저장
        print(f"상품명: {product['name']}, 할인 가격: {discounted_price}, 재고: {product['inventory']}")
        #할인한 가격(discounted_price)을 포함한 문구 출력

  elif menu == 4: #위에서 입력받은 메뉴가 4라면
    print("이용해주셔서 감사합니다.") #종료 안내 문구 출력
    break #메뉴 반복문 종료

  else: #위에서 입력받은 메뉴가 1 ~ 4 중 아무것도 아니라면
    print("지원하지 않는 시스템 입니다.") #안내 문구 출력 후 되돌아감