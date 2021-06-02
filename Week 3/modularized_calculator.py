def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readMultiply(line, index):
  token = {'type' : 'MULTIPLY'}
  return token, index + 1

def readDivide(line, index):
  token = {'type' : 'DIVIDE'}
  return token, index + 1


def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMultiply(line, index)
    elif line[index] == '/':
      (token, index) = readDivide(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def evaluate(tokens):
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  product= []
  product.insert(0, {'type': 'PLUS'})
  while index < len(tokens): # calculate multiplication and division
    if tokens[index]['type'] == 'MULTIPLY':
      product.append({'type': 'NUMBER', 'number': product[-1]['number']*tokens[index + 1]['number']})
      product.pop(-2)
      index += 2
    elif tokens[index]['type'] == 'DIVIDE':
      product.append({'type': 'NUMBER', 'number': product[-1]['number']/tokens[index + 1]['number']})
      product.pop(-2)
      index += 2
    else:
      product.append(tokens[index])
      index += 1
  print(product)
  
  index = 1
  while index < len(product):
    if product[index]['type'] == 'NUMBER':
      if product[index - 1]['type'] == 'PLUS':
        answer += product[index]['number']
      elif product[index - 1]['type'] == 'MINUS':
        answer -= product[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer


def test(line):
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("1*2+4*3/2")
  test("1/3*2/3")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
