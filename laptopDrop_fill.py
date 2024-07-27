#결측치 처리

import pandas as pd
import numpy as np

LapTop = pd.DataFrame({
  "브랜드": ["삼성", "엘지", "레노버", "애플", "HP"],
  "가격": [200, 250, 300, 400, np.nan],
  "평점": [4, 4, 3, np.nan, 2],
  "판매율": [60, 63, np.nan, np.nan, 52]
})

#결측치값이 있는 행 제거
LapTop_dropped = LapTop.dropna()

#특정 열에서만 결측값이 있는 행 제거
LapTop_subset = LapTop.dropna(subset=['판매율'])

#모든 결측값 "정보없음"으로 채우기
LapTop_filled = LapTop.fillna("정보없음")

#모든 결측값에 임시 값으로 채우기
values = {"가격": 200, "평점": 2, "판매율": 50}
LapTop_anotherFilled = LapTop.fillna(value=values)

#모든 브랜드의 평균 가격 구하기
LapTopAvg = LapTop_anotherFilled['가격'].mean()

print(f"원본 데이터:\n {LapTop}")
print(f"\n결측치 행 제거:\n {LapTop_dropped}\n")
print(f"\n판매율에서 결측치 행 제거:\n {LapTop_subset}\n")
print(f"\n모든 결측값 '정보없음'으로 채우기:\n {LapTop_filled}\n")
print(f"\n모든 결측값에 임시 값 채우기:\n {LapTop_anotherFilled}\n")
print(f"\n임시 값을 채운 데이터로 평균 가격 구하기:\n {LapTopAvg}\n")


#평점 계산해서 추가하기
def LapTopGPA(row):
    if row['평점'] > 3 and row['판매율'] >= 60:
        return "높음"
    else:
        return "낮음"

LapTop["선호도"] = LapTop.apply(LapTopGPA, axis=1)


print(f"\n선호도 추가한 데이터:\n {LapTop}")