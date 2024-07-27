import pandas as pd

data = pd.DataFrame({
    '이름': ["홍길동", "황진이", "이순신", "김유신", "유관순"],
    '학급': ["A", "A", "B", "B", "A"],
    '성별': ["남", "여", "남", "남", "여"],
    '수학 점수': [85, 92, 78, 88, 95],
    '영어 점수': [90, 85, 93, 80, 87]
}, index = [1, 2, 3, 4, 5])

data2 = pd.DataFrame({
    '이름': ["새싹", "영등포", "양천구", "강서구", "구로구"],
    '학급': ["A", "A", "B", "A", "B"],
    '성별': ["여", "남", "여", "남", "여"],
    '수학 점수': [75, 84, 93, 63, 55],
    '영어 점수': [83, 73, 82, 72, 92]
}, index = [1, 2, 3, 4, 5])

#초기 데이터
totalData = pd.concat([data, data2], ignore_index=True)

#자르기
sliced_data = totalData.loc[1:3, '이름':'수학 점수']

#수학, 영어 점수별로 sort하기
mathScore = totalData.loc[::].sort_values(by='수학 점수')
engScore = totalData.loc[::].sort_values(by='영어 점수')

#성별, 학급별로 점수 합과 평균 구하기
math_and_eng = totalData.groupby('성별').agg({'수학 점수': ['sum', 'mean'], '영어 점수': ['sum', 'mean']})
class_mathAndEng = totalData.groupby('학급').agg({'수학 점수': ['sum', 'mean'], '영어 점수': ['sum', 'mean']})

#학급 데이터 round로 소수점 1개까지 출력
class_mathAndEng = class_mathAndEng.round(1)

#최종 출력
print(f"초기 데이터 \n{totalData.sort_values(by='성별')}")
print(f"\n행 따라서 자르기\n{sliced_data}")
print(f"\n성별로 나누어서 \n{math_and_eng}")
print(f"\n학급으로 나누어서 \n{class_mathAndEng}")