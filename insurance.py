#보험 청구서 처리

#보험 청구서에서 필요한 정보를 추출

import re

insuranceBill = """
보험 청구서

환자 이름: 홍길동
환자 ID: 123456789
생년월일: 1985-05-20
주소: 서울특별시 강남구 역삼동 123-45

청구 내역:
---------------------------------
진료 날짜: 2024-07-01
병명: 감기
비용: 50,000원

진료 날짜: 2024-07-02
병명: 알레르기
비용: 30,000원

진료 날짜: 2024-07-05
병명: 두통
비용: 20,000원
---------------------------------

총 청구 금액: 100,000원
보험 회사: Sesac 보험
보험 번호: INS1234567
"""

def extractInfo(extract):
  info = {} #info를 딕셔너리로 선언

  info["환자 이름"] = re.search(r'환자 이름:\s*(.*)', extract).group(1)
  #extract에서 공백을 무시하고 뒤에 있는 임의의 문자열을 추출하여 info["환자 이름"]에 저장
  info["생년월일"] = re.search(r'생년월일:\s*([\d-]+)', extract).group(1)
  #위와 같이 공백 무시 -> 숫자와 하이픈이 1개 이상있는 문자열을 추출하여 저장
  info["주소"] = re.search(r'주소:\s*(.*)', extract).group(1)
  #맨 위 ["환자 이름"]과 동일한 방식

  info["진료 내역"] = re.findall(r'진료 날짜:\s*([\d-]+)\s*병명:\s*(\S+)\s*비용:\s*([\d,]+)원', extract)
  #공백 무시하고 숫자와 하이픈이 있는 1개 이상의 문자열(진료 날짜)
  #~~ 무시하고 공백이 아닌 문자 1개 이상의 문자열(병명)
  #~~~ 숫자와 ,가 1개 이상의 문자열 (비용)

  ##findall은 매칭되는 모든 패턴들을 찾아 리스트로 반환한다.
   ##(= 전체 문자열에서 정규 표현식으로 매칭되는 모든 패턴을 찾음)
  ##패턴이 그룹에 포함되어 있으면 해당 그룹의 값들로 이루어진 튜플로 반환
    ##위에서 찾은(매칭된) 패턴을 그룹으로 분할되어 튜플로 반환
    ###-> 매칭된 패턴의 리스트가 info["진료 내역"]에 저장됨
  ### -> 따로 그룹으로 추출할 필요 없음!
  ####info["진료 내역"]만 따로 출력하면 [(이런 식으로 출력됨)] => 리스트 안에 튜플이 들어간

  info["총 청구 금액"] = re.search(r'총 청구 금액:\s*([\d,]+)원', extract).group(1)
  #~~~~ 숫자와 ,가 1개 이상의 문자열을 추출 ~~
  info["보험 회사"] = re.search(r'보험 회사:\s*(.*)', extract).group(1)
  #~~~~ 임의의 문자열을 ~~~~
  info["보험 번호"] = re.search(r'보험 번호:\s*(\S+)', extract).group(1)
  #~~~~ 공백이 아닌 문자열을 ~~~~

  return info

extractedInfo = extractInfo(insuranceBill)

print("🌱보험 청구 시 필요한 정보🌱\n")
for key, value in extractedInfo.items():
  if key == "진료 내역":
    print(f"{key}:")
    for detail in value:
      print(f"  - 진료 날짜: {detail[0]}, 병명: {detail[1]}, 비용: {detail[2]}")
      ##위에서 말했듯이 info["진료 내역"]은 리스트 안에 튜플로 묶여서 저장이 되었기 때문에 출력하면 [(이렇게 됨)]
      ###따라서 따로 for문으로 값을 출력해줘야 함
  else:
    print(f"{key}: {value}")