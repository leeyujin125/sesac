import pandas as pd

joseonStudents = pd.DataFrame({
    '황진이': [100, 98, 95, 99, 100],
    '홍길동': [80, 78, 83, 62, 68],
    '집가고': [65, 26, 62, 45, 25],
    '싶어엌': [58, 39, 69, 29, 49]
}, index = ["국어", "사회", "역사", "수학", "과학"])

sesacStudents = pd.DataFrame({
    '새싹': [96, 96, 94, 96, 94],
    '크헝헝': [46, 27, 37, 74, 36],
    '굼뱅이': [83, 54, 73, 21, 67],
    '지렁이': [93, 26, 47, 57, 37],
}, index = ['국어', '사회', '역사', '수학', '과학'])

#studentsSubjectCombine = pd.concat([joseonStudents, sesacStudents], axis=1) #concat 이용
studentsSubjectCombine = pd.merge(joseonStudents, sesacStudents, left_index=True, right_index=True, how='outer') #merge 이용

def randomStudent():
  sampleStudents = studentsSubjectCombine.sample(n=3, axis=1)
  print("조선 학생들과 새싹 학생들 중 랜덤한 학생 3명을 출력합니다!")
  print(sampleStudents)

def certainStudent():
  certainInput = input("검색하려는 학생의 이름을 입력하세요: ")
  if certainInput in studentsSubjectCombine.columns:
      certainStudent = studentsSubjectCombine[certainInput]
      print("검색하신 학생의 정보 입니다.")
      print(certainStudent)
  else:
      print(f"{certainInput} 학생이 데이터에 없습니다.")

def certainSubject():
  searchSubject = input("검색하실 과목 이름을 입력하세요: ")
  if searchSubject in studentsSubjectCombine.index:
    findSubject = studentsSubjectCombine.loc[searchSubject]
    print("검색하신 과목의 학생들 점수 입니다.")
    print(findSubject)
  else:
    print(f"{searchSubject}가 데이터에 없습니다.")

def certainScore():
  scoreInput = int(input("검색하실 점수를 입력하세요: "))
  score = studentsSubjectCombine.isin([scoreInput])
  result = studentsSubjectCombine.apply(lambda x: x[x == scoreInput].dropna(), axis=1)
  #result = studentsSubjectCombine.mask(studentsSubjectCombine != scoreInput)
  print(f"검색하신 {scoreInput}점을 받은 학생들 입니다.")
  print(result.dropna(how='all'))

print("조선 학생들과 새싹 학생들 목록\n")
print(studentsSubjectCombine)

while True:

  menu = int(input("1. 랜덤 출력   2. 학생 검색   3. 과목 검색   4. 점수 검색    5. 끝내기"))

  if menu == 1:
    randomStudent()
  elif menu == 2:
    certainStudent()
  elif menu == 3:
    certainSubject()
  elif menu == 4:
    certainScore()
  elif menu == 5:
    break
  else:
    print("다시 입력")

print(studentsSubjectCombine.describe())