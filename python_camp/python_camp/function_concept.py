# --------------------------------------------
# 1. 함수의 다양한 입력들 살펴보기 
#
# 1) input이 없는 함수 
# 2) input이 여러 개 있는 함수 
# 3) input이 정해지지 않은 갯수만큼 있는 함수 
# --------------------------------------------

def pi():
    """원주율을 소숫점 두 자리까지 반환하는 함수
    """
    import math
    print("함수 pi 호출")
    pi = "%0.2f" % math.pi
    return pi

print(pi())

def left_append(lst, elem):
    """lst의 왼쪽에 elem을 넣고, lst를 반환하는 함수 
    """
    print("함수 left_append 호출")
    lst.insert(0, elem)
    return lst

lst = ["Python", "Javascript", "SQL"]
new_elem = "HTML5"
print(left_append(lst, new_elem))

def left_extend(lst, *elem):
    """lst의 왼쪽에 정해지지 않은 갯수의 elem을 넣고 lst를 반환하는 함수 
    """
    print("함수 left_extend 호출")
    for em in elem:
        lst.insert(0, em)
    return lst 

lst = ["*args", "이용해서", "여러개"]
new_em = "Input"
new_em2 = "print"
new_em3 = "end"
print(left_extend(lst, new_em, new_em2, new_em3))

# --------------------------------------------
# 2. 함수의 call stack 알아보기 
# 
# 1) 아래 함수 b()를 실행할 때, 실행된 함수의 순서는?
# --------------------------------------------

def a():
    print("함수 a 호출")
    return pi()

def b():
    print("함수 b 호출")
    return a()

b()
print("58에서 실행 -> 54 -> 55 -> 56 -> 50 -> 51 -> 52 -> 9로가서 pi함수 실행")

# --------------------------------------------
# 2) 아래 함수 c()를 실행할 때, 실행된 함수의 순서와 각 함수의 input은? 
# --------------------------------------------

def c(lst):
    if not lst:
        return False
    
    print(lst[0])
    return c(lst[1:]) 

c(list(range(10)))

# 45 -> 40 -> 41 -> 43
# 출력: 0 1 2 3 4 5 6 7 8 9 IndexError: list index out of range

print("수정한 코드 출력 -> 72 -> 65 -> 66 -> 69 -> 70")