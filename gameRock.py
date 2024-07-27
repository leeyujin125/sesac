
import random

print("컴퓨터와 가위 바위 보!")
print()

game_mapping = {
    1 : '가위',
    2 : '바위',
    3 : '보'
}

attempts = 0 #게임 횟수 카운트

user_win = 0
user_lose = 0

computer_win = 0
computer_lose = 0

while True:
  computer_choice = random.randint(1, 3)
  user_choice = input("가위 바위 보 | 입력 >>> ")
  print()

  if user_choice not in game_mapping.values():
    print("제대로 입력!")
    continue

  if user_choice == game_mapping[computer_choice]:
        attempts += 1
        print(">>비겼습니다. 다시 도전!<<")
        print()
  elif (user_choice == "가위" and game_mapping[computer_choice] == "바위") or \
        (user_choice == "바위" and game_mapping[computer_choice] == "보") or \
        (user_choice == "보" and game_mapping[computer_choice] == "가위"):
        attempts += 1
        user_lose += 1
        computer_win += 1
        print(f">>컴퓨터는 {game_mapping[computer_choice]}를 선택! 아쉽네요~<<")
        print()
  else:
        attempts += 1
        user_win += 1
        computer_lose += 1
        print(f">>컴퓨터는 {game_mapping[computer_choice]}를 선택! 축하합니다~<<")
        print()
  if attempts >= 5:
        print("게임 끝! 점수를 공개합니다~")
        print()
        print(f"컴퓨터 : 승리 => {computer_win} 패배 => {computer_lose}")
        print()
        print(f"사용자 : 승리 => {user_win} 패배 => {user_lose}")
        print()
        print(f"총 {attempts}의 횟수를 사용하였습니다.")
        break