#리스트, 튜플, 딕셔너리 한꺼번에 사용해보기

#환자 관리 시스템 (환자 조회 및 추가, 증상 관리, 차트번호 관리, 정보 수정 및 삭제)

import random

patients = {
    "홍길동" : {
        "증상" : ["미열", "복통", "설사"],
        "차트번호" : (1502)
    },
    "앨리스" : {
        "증상" : ["두통", "미열", "기침"],
        "차트번호" : (2304)
    },
    "나나" : {
        "증상" : ["고열", "기침", "호흡곤란"],
        "차트번호" : (4101)
    },
    "쉐리" : {
        "증상" : ["이통", "두통", "어지럼증"],
        "차트번호" : (2950)
    },
    "나비" : {
        "증상" : ["어지럼증", "두통", "이명"],
        "차트번호" : (5892)
    }
}

def printPatients():
  """전체 환자 정보 출력"""
  for name, info in patients.items():
    symptoms = ", ".join(info["증상"])
    chart_number = info["차트번호"]
    print(f"환자 이름: {name}, 증상: {symptoms}, 차트번호: {chart_number}")

def generateUniqueChartNumber():
    """차트번호 중복 체크 후 랜덤으로 생성"""
    existing_chart_numbers = [info["차트번호"] for info in patients.values()]
    while True:
        new_chart_number = random.randint(1000, 9999)
        if new_chart_number not in existing_chart_numbers:
            return new_chart_number

def printPatientsInfo(name):
    """특정 환자 정보 출력"""
    if name in patients:
        info = patients[name]
        symptoms = ", ".join(info["증상"])
        chart_number = info["차트번호"]
        print(f"환자 이름: {name}, 증상: {symptoms}, 차트번호: {chart_number}")
    else:
        print(f"{name}님께서는 본 의원에서 진료받으신 기록이 없으십니다.")

while True:
    print("🌱 새싹 이비인후과 입니다. 원하시는 메뉴를 클릭해주세요! 🌱")
    print("1. 환자 조회")
    print("2. 신환 등록")
    print("3. 증상 관리")
    print("4. 차트 수정")
    print("5. 종료")

    try:
        menu = int(input("메뉴를 선택하세요:"))
        if menu == 1:
            print("🌱환자 조회🌱")
            detailsMenu = input("전체 환자 조회는 1번, 특정 환자 조회는 2번: ")
            if detailsMenu == "1" or detailsMenu == "1번":
                printPatients()
            elif detailsMenu == "2" or detailsMenu == "2번":
                searchPatient = input("환자 성함을 입력해주세요: ")
                printPatientsInfo(searchPatient)
            else:
                print("유효하지 않은 입력입니다.")

        elif menu == 2:
            print("🌱신환 등록🌱")
            newPatientsName = input("등록하실 환자 성함을 입력하세요: ")
            newPatientsSymptoms = input("주 증상을 입력하세요 (쉼표로 구분): ")
            newPatientsSymptoms2 = [name.strip() for name in newPatientsSymptoms.split(",")]
            newPatientsNumber = generateUniqueChartNumber()

            patients[newPatientsName] = {
                "증상" : newPatientsSymptoms2,
                "차트번호" : newPatientsNumber
            }

            print("신환 등록 성공!")

        elif menu == 3:
            print("🌱증상 관리🌱")
            SymptomAdmin = input("증상을 변경 혹은 삭제할 환자 이름을 입력하세요: ")
            if SymptomAdmin in patients:
                detailsSymptomAdmin = input("증상 변경은 변경, 추가는 추가, 삭제는 삭제를 입력하세요: ")
                if detailsSymptomAdmin == "추가":
                    inputSymptom = input("추가하려는 증상을 입력하세요 (여러 개는 쉼표로 구분): ")
                    inputSymptom2 = [name.strip() for name in inputSymptom.split(",")]
                    patients[SymptomAdmin]["증상"].extend(inputSymptom2)
                    print("증상 추가 완료!")
                elif detailsSymptomAdmin == "변경":
                    print(f"현재 {SymptomAdmin}님의 증상: {patients[SymptomAdmin]['증상']}")
                    changeIndex = int(input("변경할 증상의 번호를 선택하세요 (앞에서 부터 1번): ")) - 1
                    changeSymptom = input("변경할 증상을 입력하세요: ")
                    patients[SymptomAdmin]["증상"][changeIndex] = changeSymptom
                    print("증상 변경 완료!")
                elif detailsSymptomAdmin == "삭제":
                    print(f"현재 {SymptomAdmin}님의 증상: {patients[SymptomAdmin]['증상']}")
                    deleteSymptom = input("삭제할 증상을 입력하세요: ")
                    if deleteSymptom in patients[SymptomAdmin]["증상"]:
                        patients[SymptomAdmin]["증상"].remove(deleteSymptom)
                        print("증상 삭제 완료!")
                    else:
                        print("입력한 증상이 존재하지 않습니다.")
                else:
                    print("유효하지 않은 서비스 입니다.")
            else:
                print(f"{SymptomAdmin}님께서는 본 의원에서 진료 받으신 기록이 없습니다.")

        elif menu == 4:
            print("🌱차트 수정🌱")
            patientAdmin = input("이름 변경을 원하시는 환자 성함을 입력해주세요 (증상 관리는 3번으로): ")
            if patientAdmin in patients:
                detailsAdmin = input("환자 성함을 변경하시겠습니까? (네, 아니요): ")
                if detailsAdmin == "네":
                    changeName = input("변경 원하시는 성함을 입력해주세요: ")
                    patients[changeName] = patients.pop(patientAdmin)
                    print(f"{patientAdmin}님의 성함이 {changeName}으로 변경되었습니다.")
                elif detailsAdmin == "아니요":
                    print("증상에 관한 수정은 3번으로 가주세요. 차트 번호는 수정이 불가능 합니다.")
                else:
                    print("유효하지 않은 서비스 입니다.")
            else:
                print(f"{patientAdmin}님께서는 본 의원에서 진료 받으신 기록이 없습니다.")

        elif menu == 5:
            print(" 🌱 새싹 이비인후과를 이용해주셔서 감사합니다. 🌱 ")
            break

        else:
            print("유효하지 않는 서비스 입니다.")

    except ValueError:
        print("숫자를 입력해주세요.")