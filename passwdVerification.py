import re

def pwVerification(password):
  if(len(password) >= 8 and
     re.search(r'[A-Z]', password) and
     re.search(r'[a-z]', password) and
     re.search(r'[0-9]', password) and
     re.search(r'[\W_]', password)):
     return "보안성 높음"
  elif(len(password) >= 8 and
      re.search(r'[A-Za-z]', password) and
      re.search(r'\d', password)):
      return "보안성 낮음. 특수문자를 추가하세요."

  elif(len(password) >= 8 and
      re.search(r'[A-Z\d]', password) and
      re.search(r'\W', password)):
      return "보안성 낮음. 소문자를 추가하세요."

  elif(len(password) >= 8 and
      re.search(r'[a-z\d]', password) and
      re.search(r'\W', password)):
      return "보안성 낮음. 대문자를 추가하세요."

  elif(len(password) >= 8 and
      re.search(r'[A-Za-z\W]', password)):
      return "보안성 낮음. 숫자를 추가하세요."

  else:
    return "보안성 낮음"

while True:
  passwords = input("생성할 비밀번호를 입력해주세요 (대소문자, 특수문자 포함하여 8자 이상): ")

  if len(passwords) < 8:
    print("비밀번호는 8자 이상 입력하세요.")

  else :
    verificationCompleted = pwVerification(passwords)
    print(f"{passwords}의 {verificationCompleted}")
    break