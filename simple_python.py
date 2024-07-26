#실습예제

#text 마지막 줄이 =(assignment)가 아니면 계산 값 리턴
#맞으면 None 리턴
#만약 계산 불가하면 raise Name Error

simple_python = """
exam = 1
exam2 = 2 
exam + exam2 + 3
"""

def eval_simple_python(text):
  lines = text.split('\n')

  namespace = {}
  res = None

  for line in lines:
    res, namespace = eval_line(line, namespace)

  return res


def eval_line(line, namespace):
  if is_assingment(line):
    name, value = parse_assignment(line)
    namespace[name] = value
    return None, namespace
  elif is_expression(line):
    value = eval_expression(line)
    return value, namespace
  
  return value, namespace

def is_assingment(line):
  if '=' in line:
    left, right = line.split('=')
    name = left.strip() #check if name is valid ex) 123 = 123
    expr = right.strip()

    
def is_expression(line):
  return not is_assingment(line)

def parse_assignment(line, namespace):
  left, right = line.split('=')
  name = left.strip() #check if name is valid ex) 123 = 123
  expr = right.strip()
  
  value = eval_expression(expr, namespace)

def eval_expression(line, namespace):
  values = line.split('+')
  values = [v.strip() for v in values]

  result = 0

  for v in values:
    if v.isnumeric(): #문자열인데 숫자같은 애인지?
      result += int(v)
    else:
      if v in namespace:
        result += namespace[v]
      else:
        raise NameError

# print(eval_simple_python(simple_python))