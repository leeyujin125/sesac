# 진료 예약 시스템

# 예약된 진료 시간을 저장할 딕셔너리
appointments = {}

def reserve_appointment(doctor_name, patient_name, appointment_date, appointment_time):
    """
    진료 예약을 처리하는 함수

    Args:
    - doctor_name (str): 의사 이름
    - patient_name (str): 환자 이름
    - appointment_date (str): 예약 날짜 (YYYY-MM-DD 형식)
    - appointment_time (str): 예약 시간 (HH:MM 형식)

    Returns:
    - str: 예약이 성공적으로 처리되었음을 알리는 메시지
    """
    # 예약 날짜와 시간을 키로 사용하여 예약 정보를 저장
    appointment_key = (appointment_date, appointment_time)
    appointments[appointment_key] = (doctor_name, patient_name)

    return f"{appointment_date} {appointment_time}에 {doctor_name} 의사의 진료가 예약되었습니다. 환자: {patient_name}"

# 예약을 시도할 정보 입력 받기
doctor_name = input("의사 이름을 입력하세요: ")
patient_name = input("환자 이름을 입력하세요: ")
appointment_date = input("예약 날짜를 입력하세요 (YYYY-MM-DD): ")
appointment_time = input("예약 시간을 입력하세요 (HH:MM): ")

# 진료 예약 함수 호출
reservation_message = reserve_appointment(doctor_name, patient_name, appointment_date, appointment_time)

# 예약 결과 출력
print(reservation_message)

# 예약된 진료 시간 확인
print("현재 예약된 진료 시간:")
for key, value in appointments.items():
    print(f"{key[0]} {key[1]} - 의사: {value[0]}, 환자: {value[1]}")