def calculateArea(shape, *dimensions):
  if shape == '사각형':
    length, width = dimensions
    area = length * width
  elif shape == '원형':
    radius, = dimensions
    area = 3.14 * radius ** 2
  elif shape == '삼각형':
    base, height = dimensions
    area = 0.5 * base * height
  else:
    return f"지원하지 않는 도형입니다: {shape}"
  return area

while True:
  user_shapes = input("원하시는 도형의 이름을 적어주세요 (끝내고 싶다면 'done'을 입력하세요.): ")
  if user_shapes.lower() == 'done':
    break
  if user_shapes == '사각형':
    user_length = int(input("길이가 어떻게 되나요? "))
    user_width = int(input("가로 높이는 어떻게 되나요? "))

    area = calculateArea(user_shapes, user_length, user_width)
    print(f"원하시는 도형 {user_shapes}의 넓이는 {area} 입니다! ")
  elif user_shapes == '원형':
    user_radius = int(input("원의 반지름이 어떻게 되나요? "))

    area = calculateArea(user_shapes, user_radius)
    print(f"원하시는 도형 {user_shapes}의 넓이는 {area} 입니다! ")
  elif user_shapes == '삼각형':
    user_base = int(input("삼각형의 밑변을 알려주세요. "))
    user_height = int(input("삼각형의 높이를 알려주세요. "))

    area = calculateArea(user_shapes, user_base, user_height)
    print(f"원하시는 도형 {user_shapes}의 넓이는 {area} 입니다! ")
  else:
    print("잘못 입력하신 것 같아요!")
    continue