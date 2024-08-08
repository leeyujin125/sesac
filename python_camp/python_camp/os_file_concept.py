import os 
import pickle 

# --------------------------------------------
# 1. os 기초 예제 
# 
# 1) os.path 이해하기 (os.path.exists, os.path.join, os.path)
# 2) os.listdir #dir 출력 / os.makedirs #dir 만들기 해보기 
# 3) os.getcwd #현재 위치 / os.changedir #dir 바꾸기? 해보기 
# --------------------------------------------

# print(os.getcwd())

for elem in os.listdir():
  if os.path.isdir(elem):
    print('<DIR>\t\t' + elem)
  elif '.' in elem:
    extension = elem.split('.')[-1]
    print(f"{extension}    \t\t{elem}")
  
  
def create_dir(directory_name):
  if not os.path.exists(directory_name): #존재하냐 -> 존재한다 True
    print(f"{directory_name} does not exists;")
    os.makedirs(directory_name)
  else:
    print(f"{directory_name} does exists;")

  
# create_dir('test_dir') # return이 없어서 None이지만 함수를 호출하기만 해서 None값 반환 안함
# --------------------------------------------
# 2. file 기초 예제 
# 
# 1) open 이해하기 
# 2) 파일 읽기, 써보기 
# --------------------------------------------
# w -> write / r -> read / w+ -> 없다면 만들어서 쓰겠다. ,기존 내용 없애고 덮어쓴다. / a -> 기존 내용 유지 (append)
# encoding = 'utf-8'
from time import time #작동하는데 얼마나 걸렸는지

begin = time()
f = open('example.txt', 'w+', encoding='utf-8')

# for i in range(1000000000):
#   print(str(i) * 10000, file = f)

# f. close()
end = time()
print(f"{end-begin} sec passed for making example.txt")
f = open('example.txt', 'r', encoding='utf-8')

# for i in range(100):
#   # print(i, file = f)
#   f.write(str(i) + '\n')

print(f.readline())
print(f.readline())
for line in f.readlines():
  print(line)

f.close()

# --------------------------------------------
# 3. pickle 기초 예제  -> lambda는 안됨. 모든 오브젝트가 피클이 되는건 아님 
# 
# 1) pickle.load() 해보기 
# 2) pickle.dump() 해보기 
# --------------------------------------------

d = "0과 1 비트로 저장됨"

pickle.dump(d, open('empty_dict.pickle', 'wb+')) #0과 1로 이루어진 dump로 저장하겠다.

e = pickle.load(open('empty_dict.pickle', 'rb')) #b는 바이트를 의미

print(e)