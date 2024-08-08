import random 

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------

length = 5

listTuple = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(length)]
print("🌱🌱🌱original List:",listTuple,'🌱🌱🌱\n')



def tupleSum(lst): # 숫자 두 개의 합이 제일 큰 튜플
  max_sum = lst[0][0] + lst[0][1]
  max_tuple = lst[0]

  for item in lst[1:]:
    current_sum = item[0] + item[1]
    if max_sum < current_sum:
      max_sum = current_sum
      max_tuple = item

  return max_tuple

def tupleWhich(lst): # 두 개의 숫자 중 첫 번째 숫자가 제일 큰 튜플
  
  max_value = lst[0][0]
  max_tuple = lst[0]

  for item in lst[1:]:
    current_which = item[0]
    if max_value < current_which:
      max_value = current_which
      max_tuple = item

  return max_tuple

def my_max(lst, cmp = lambda x, y : x): # 어떤 조건이 주어져도 돌아가도록
  max_value = lst[0]

  for item in lst[1:]:
    if cmp(max_value, item) == item:
      max_value = item

  return max_value

def my_min(lst, cmp = lambda x, y : x):
  min_value = lst[0]

  for item in lst[1:]:
    if cmp(min_value, item) == min_value:
      min_value = item
  
  return min_value


print("SumMax:",my_max(listTuple, cmp = lambda x, y: x if sum(x) > sum(y) else y))
print("WhichMax",my_max(listTuple, cmp = lambda x, y: x if x[0] > y[0] else y),'\n')

print("SumMin:",my_min(listTuple, cmp = lambda x, y: x if sum(x) > sum(y) else y))
print("WhichMin:",my_min(listTuple, cmp = lambda x, y: x if x[0] > y[0] else y),'\n')

# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 2) 오름차순, 내림차순으로 정렬하기 
# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기 
# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기 
# --------------------------------------------

# 1) 그냥 순서대로 오름차순
print("===========================")
lst = list([random.randint(1, 30) for _ in range(10)])
print("🌱🌱🌱sort1 -> original List:",lst,"🌱🌱🌱")

def sort1another(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

sorted_lst = sort1another(lst)
print("sort1 another -> sorted List:", sorted_lst)
print("===========================\n")

def sort1(lst):
    res = []
    n = len(lst)
    while len(res) < n:
        res.append(my_min(lst, cmp = lambda x, y : min(x,y)))
        lst.remove(my_min(lst, cmp = lambda x, y : min(x,y)))
    return res 

print("sort1 origianl:", sort1(lst))
print("===========================\n")

# 2) 오름차순, 내림차순 
sort_lst = list([random.randint(1, 30) for _ in range(10)])
print("🌱🌱🌱sort2 -> original List:", sort_lst,"🌱🌱🌱")

def sort2another(lst, upper_to_lower = True): #True면 내림차순 / False면 오름차순 
    n = len(lst)
    for i in range(n):
       for j in range(0, n-i-1):
          if upper_to_lower == True:
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
          else:
             if lst[j+1] < lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

print("sort2 another True ->",sort2another(sort_lst, upper_to_lower=True))
print("sort2 another False ->",sort2another(sort_lst, upper_to_lower=False))
print("===========================\n")

def sort2(lst, upper_to_lower = True):
  res = []
  n = len(lst)
  temp_list = lst[:]
  while len(res) < n:
    if upper_to_lower == True:
      min_val = my_min(temp_list, cmp = lambda x, y: min(x, y))
      res.append(min_val)
      temp_list.remove(min_val)
    else:
      max_val = my_min(temp_list, cmp = lambda x, y: max(x, y))
      res.append(max_val)
      temp_list.remove(max_val)
  return res

print("sort2 original True:", sort2(sort_lst, True))
print("sort2 original False:", sort2(sort_lst, False))
print("===========================\n")

# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬
sortByCmp = [random.randint(1, 50) for _ in range(10)]
print("🌱🌱🌱sort3 -> original List:", sortByCmp,"🌱🌱🌱")

def sort3(lst, upper_to_lower = True, cmp = lambda x, y: x):
    res = []
    n = len(lst)
    temp_list = lst[:]
    while len(res) < n:
        if upper_to_lower == True:
            min_val = my_min(temp_list, cmp = lambda x, y: min(x, y))
            res.append(min_val)
            temp_list.remove(min_val)
        else:
            max_val = my_min(temp_list, cmp = lambda x, y: max(x, y))
            res.append(max_val)
            temp_list.remove(max_val)
    return res

print("sort3 True:",sort3(sortByCmp, True, cmp = lambda x, y: x if x[0] > y[0] else y))
print("sort3 False:",sort3(sortByCmp, False, cmp = lambda x, y: x if sum(x) > sum(y) else y))
print("===========================\n")

# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력
randomList = [random.randint(1, 50) for _ in range(10)]
randomList2 = [random.randint(1, 50) for _ in range(10)]

def sort4(lst, upper_to_lower = True, cmp = lambda x, y: x):



    return

print("sort4 True:", sort4(randomList, True, cmp = lambda x, y: x if x[0] > y[0] else y))

# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기

randomLst = [random.randint(1, 50) for _ in range(10)]
randomLst2 = [random.randint(1, 50) for _ in range(10)]

def sort5(lst, upper_to_lower=True, cmp=lambda x, y: x > y, tie_breaker=lambda x, y: random.choice([x, y])):
    n = len(lst)

    def demo_sort5(x, y):
        if cmp(x, y):
            return True
        elif cmp(y, x):
            return False
        else:
            return tie_breaker(x, y) == x

    for i in range(n):
        for j in range(0, n - i - 1):
            if upper_to_lower:
                if demo_sort5(lst[j], lst[j + 1]):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else:
                if demo_sort5(lst[j + 1], lst[j]):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

sort_lst = [(1, 4), (1, 5), (1, 2), (40, 24), (3, 1), (5, 4), (1, 3),(3,3)]
sort_lst_desc = sort5(
    sort_lst.copy(),
    upper_to_lower=True,
    cmp=lambda x, y: (x[0] > y[0]) or (x[0] == y[0] and x[1] > y[1]),
    tie_breaker=lambda x, y: random.choice([x, y])
)
print(f'내림차순: {sort_lst_desc}')



# --------------------------------------------
# os_file_concept.py 해보고 올 것 
# --------------------------------------------

# --------------------------------------------
# 3. safe pickle load/dump 만들기 
# 
# 일반적으로 pickle.load를 하면 무조건 파일을 읽어와야 하고, dump는 써야하는데 반대로 하면 굉장히 피곤해진다. 
# 이런 부분에서 pickle.load와 pickle.dump를 대체하는 함수 safe_load, safe_dump를 짜 볼 것.  
# hint. 말만 어렵고 문제 자체는 정말 쉬운 함수임.
# --------------------------------------------

def safe_load(pickle_path):
    pass 

def safe_dump(pickle_path):
    pass 


# --------------------------------------------
# 4. 합성함수 (추후 decorator)
# 
# 1) 만약 result.txt 파일이 없다면, 함수의 리턴값을 result.txt 파일에 출력하고, 만약 있다면 파일 내용을 읽어서 
#    '함수를 실행하지 않고' 리턴하게 하는 함수 cache_to_txt를 만들 것. txt 파일은 pickle_cache 폴더 밑에 만들 것.  
# 2) 함수의 실행값을 input에 따라 pickle에 저장하고, 있다면 pickle.load를 통해 읽어오고 없다면 
#    실행 후 pickle.dump를 통해 저장하게 하는 함수 cache_to_pickle을 만들 것. pickle 파일은 pickle_cache 폴더 밑에 만들 것. 
# 3) 함수의 실행값을 함수의 이름과 input에 따라 pickle에 저장하고, 2)와 비슷하게 진행할 것. pickle 파일은 pickle_cache 폴더 밑에, 
#    각 함수의 이름을 따서 만들 것 
# --------------------------------------------

def cache_to_txt(function):
    pass 

def cache_to_pickle(function):
    pass 


