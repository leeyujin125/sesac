all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'

# --------------------------------------------
# 1. list/tuple 기초 예제들 
# 
# a는 1,2,3이 들어간 튜플, 
# b는 a부터 z까지 모든 알파벳 소문자가 들어간 리스트가 되도록 만들어보세요. 
# b를 만들 때 위에 주어진 all_smallcase_letters와 for loop를 사용해도 좋고, 손으로 다 쳐도 좋습니다. 
# --------------------------------------------

a = (1, 2, 3)
b = []
for i in all_smallcase_letters:
    b.append(i)
print(b)

# --------------------------------------------
# 2. dict 기초 예제 
# 
# 1) upper_to_lower
#
# upper_to_lower은 모든 대문자 알파벳(ex. A)을 key로 가지고, 대응하는 소문자 알파벳(ex. a)을 value로 가지는 dict입니다. 
# 위에서 만든 b와 for loop를 이용해서 upper_to_lower을 만들어보세요. 
# 
# 2) lower_to_upper
#
# upper_to_lower과 반대로 된 dict를 만들어보세요. 
# 
# 3) alpha_to_number
# 
# 소문자 알파벳 각각을 key, 몇 번째 알파벳인지를 value로 가지는 dict를 만들어보세요. 
# 위 all_smallcase_letters와 enumerate함수를 사용하세요. 
# 알파벳 순서는 1부터 시작합니다. ex) alpha_to_number['a'] = 1
# 
# 4) number_to_alphabet 
#
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 
# --------------------------------------------

# 1) upper_to_lower
upper_to_lower = {}
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(uppers)):
    upper_to_lower[uppers[i]] = all_smallcase_letters[i]

print(upper_to_lower)

# 2) lower_to_upper
lower_to_upper = {}

for i in range(len(uppers)):
    lower_to_upper[all_smallcase_letters[i]] = uppers[i]

print(lower_to_upper)

# 3) alpha_to_number
alpha_to_number={}

for i, letters in enumerate(all_smallcase_letters):
    alpha_to_number[letters] = i + 1

print(alpha_to_number)

# 4) number_to_alphabet
# 1:'aA', 2:'bB', ...
number_to_alphabet = {}

aA = []

for i in range(len(b)):
    aA.append((b[i], uppers[i]))

aA = tuple(aA)

print(aA)
print(type(aA))

for i in range(len(b)):
    number_to_alphabet[i+1] = (aA[i])

print(number_to_alphabet)
print(type(number_to_alphabet))
# --------------------------------------------
# 3. 주어진 문자열의 대소문자 바꾸기 
#
# 위 2에서 만든 dict들을 이용하여, 아래 문제들을 풀어보세요. 
#  
# 1) 주어진 문자열을 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 2) 주어진 문자열을 모두 소문자로 바꾼 문자열을 만들어보세요. 
# 3) 주어진 문자열에서 대문자는 모두 소문자로, 소문자는 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 4) 주어진 문자열이 모두 알파벳이면 True, 아니면 False를 출력하는 코드를 짜보세요. 
# --------------------------------------------

a = 'absdf123SAFDSDF'

# 1) 모두 대문자로 바꾸기
upper_a = ""
for char in a:
    if char in lower_to_upper:
        upper_a += lower_to_upper[char]
    else:
        upper_a += char

print(upper_a)

# 2) 모두 소문자로 바꾸기
lower_a = ""
for char in a:
    if char in upper_to_lower:
        lower_a += upper_to_lower[char]
    else:
        lower_a += char

print(lower_a)

# 3) 대문자는 소문자로, 소문자는 대문자로

upperAndLower_a = ""
for char in a:
    if char in lower_to_upper:
        upperAndLower_a += lower_to_upper[char]
    elif char in upper_to_lower:
        upperAndLower_a += upper_to_lower[char]
    else:
        upperAndLower_a += char

print(upperAndLower_a)

# 4) 모두 알파벳이면 True
is_alpha = a.isalpha()
print(is_alpha)
# --------------------------------------------
# 4. 다양한 패턴 찍어보기 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음 패턴을 프린트해보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------
# 1, 3, 5, 7, 9
star = "*"
height = 5

for i in range(height):
    print(' ' * (height - i - 1) + star * (2 * i + 1))

# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음 패턴을 프린트해보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

for i in range(height):
    print(' ' * (height - i) + '* ' * i)

# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음 패턴을 프린트해보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

for i in range(height):
    line = ' '.join(uppers[:i + 1])
    print(' ' * (height - i) + line)

# --------------------------------------------
# 4) 피라미드 찍어보기 - 4 
# 
# 다음 패턴을 프린트해보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------

# write your code here

# --------------------------------------------
# 5) 다음 패턴을 찍어보세요. 
# 
# *         *         * 
#   *       *       *   
#     *     *     *     
#       *   *   *       
#         * * *         
#           *           
#         * * *         
#       *   *   *       
#     *     *     *     
#   *       *       *   
# *         *         * 
# --------------------------------------------

# write your code here 

