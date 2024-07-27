import calendar #캘린더를 출력하기 위한 모듈 'calendar' 호출

def print_calendar(year, month): #print_calendar라는 이름의 함수 선언, 필수 매개변수 year와 선택 매개변수 month
    cal = calendar.TextCalendar(calendar.SUNDAY)  #일요일부터 시작하는 달력을 생성하여 cal 변수에 대입
    cal_str = cal.formatmonth(year, month)  #지정된 연도와 월의 달력을 문자열로 포맷하여 cal_str에 대입
    print(cal_str) #문자열로 포맷한 cal_str을 출력

# 연도와 월을 입력받아 달력을 출력합니다.
year = int(input("연도를 입력하세요: ")) #연도를 정수로 변환하여 입력받음
month = int(input("월을 입력하세요: ")) #월을 정수로 변환하여 입력받음
print_calendar(year, month)
#위의 입력받은 연도와 월을 print_calendar의 위치 인수와 키워드 인수로 써서 보냄
#print_calendar 함수에서 연산 후 달력이 출력 됨
