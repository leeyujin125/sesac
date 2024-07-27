#학생 성적 관리

def student_grades(studentName, sub, grades):
  print(f"😁😅 Name: {studentName} \t subject: {sub} \t grades: {grades}")

grade_system = []

while True:
  print("\n==== 메뉴 ====")
  print("1. 학생 정보 입력")
  print("2. 학생 검색")
  print("3. 학생 정보 전체 출력")
  print("4. 끝내기")
  menu = int(input("원하시는 메뉴를 입력하세요: "))

  if menu == 1:
    studentName = input("학생의 이름을 입력하세요): ")
    sub = input("과목의 이름을 입력하세요: ")
    grades = input("해당 과목의 성적을 입력하세요 (A, B, C, D, F): ")

    grade_system.append((studentName, sub, grades))

  elif menu == 2:
      search_name = input("검색할 학생의 이름을 입력하세요: ")
      found = False
      for student in grade_system:
        if student[0] == search_name:
          student_grades(*student)
          found = True
          break
      if not found:
        print(f"{search_name} 학생의 정보를 찾을 수 없습니다.")

  elif menu == 3:
      def print_all_students(students):
        print("\n전체 학생 정보 출력: ")
        for student in students:
          student_grades(*student)

  elif menu == 4:
      print("프로그램을 종료합니다.")
      break

  else:
      print("잘못된 번호입니다. 다시 입력해주세요.")
