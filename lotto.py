#로또

import random

random_module = __import__("random")

def ticketCount():
    while True:
        try:
            ticket = int(input("구매하실 로또의 갯수를 입력해주세요: "))
            if ticket > 0:
                return ticket
            else:
                print("1 이상의 숫자만 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

def lottoCreate(ticket):
    lotto = []
    for _ in range(ticket):
        lottoNumbers = random_module.sample(range(1, 60), 6)
        lotto.append(lottoNumbers)
    return lotto

def lotto_aiNumbers():
    lottoAI = []
    for _ in range(6):
        lotto_numbers = random_module.randint(1, 60)
        lottoAI.append(lotto_numbers)
    return lottoAI

def resultLotto(lottoAI, user_lotto):
    return len(set(lottoAI) & set(user_lotto))

def lottoCorrect(lottoAI, tickets):
    for index, ticket in enumerate(tickets, start=1):
        matched_numbers = resultLotto(lottoAI, ticket)
        print(f"로또 {index}번: {ticket} - 일치하는 숫자 개수: {matched_numbers}개")
        if matched_numbers == 6:
            print("🥳로또 1등 당첨!🥳")
        elif matched_numbers == 5:
            print("🥳로또 2등 당첨!🥳")
        elif matched_numbers == 4:
            print("🥳로또 3등 당첨!🥳")
        elif matched_numbers == 3:
            print("😊로또 4등 당첨!😊")
        elif matched_numbers == 2:
            print("😀로또 5등 당첨!😀")
        else:
            print("😭다음 기회에😭")
   

       
ticket = ticketCount()
tickets = lottoCreate(ticket)
lottoAI = lotto_aiNumbers()

print("\n 🍀행운을 빕니다🍀 ")
for index, ticket in enumerate(tickets, start=1):
    print(f"{index}: {ticket}")

print("\n 🎫로또 번호🎫 ")
print(f"{lottoAI}")

print("\n 🍀당첨 확인 결과🍀 ")
lottoCorrect(lottoAI, tickets)
