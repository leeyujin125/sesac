#입력받은 이메일과 전화번호 검증 후 출력
#제대로 입력한게 아니면 다시 입력받도록

import re

def emailValid(email):
  emailPattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  if re.match(emailPattern, email):
    return None
  else:
    return "이메일 형식이 올바르지 않습니다."

def phoneNumberValid(phone):
  phonePattern = r'\d{3}-\d{4}-\d{4}'
  if re.findall(phonePattern, phone):
    return None
  else:
    return "전화번호 형식이 올바르지 않습니다."


while True:

  emailError = emailValid(email)
  phoneError = phoneNumberValid(phone)

  name = input("이름을 입력하세요: ")
  email = input("이메일을 입력하세요 (gildong@example.com): ")
  if emailError:
    print(emailError)
    print("다시 입력해주세요.")
    continue

  phone = input("전화번호를 입력하세요 (010-0000-0000): ")
  if phoneError:
    print(phoneError)
    print("다시 입력해주세요.")
    continue

  print(f"{name}님의 정보")
  print(f"이메일: {email}")
  print(f"전화번호: {phone}")
  break