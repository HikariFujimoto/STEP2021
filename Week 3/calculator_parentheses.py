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

def readLeftParenthesis(line, index):
  token = {'type' : 'LEFT_PARENTHESIS'}
  return token, index + 1

def readRightParenthesis(line, index):
  token = {'type' : 'RIGHT_PARENTHESIS'}
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
    elif line[index] == '(':
      (token, index) = readLeftParenthesis(line, index)
    elif line[index] == ')':
      (token, index) = readRightParenthesis(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def evalMultDiv(tokens):
  index = 0
  product= []
  # calculate multiplication and division
  while index < len(tokens): 
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
  return product

def evalAddSub(tokens):
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  # calculate addition and subtraction
  index = 1
  answer = 0
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer


def countParenthesisAppearance(tokens):
  # start with 1 as a dummy parenthesis at beginning and end of list
  leftAppearance = 1
  rightAppearance = 1
  for index in range(len(tokens)):
    if tokens[index]['type'] == 'LEFT_PARENTHESIS':
      leftAppearance += 1
    if tokens[index]['type'] == 'RIGHT_PARENTHESIS':
      rightAppearance += 1
  if leftAppearance != rightAppearance:
    print('Imcomplete parenthesis')
    exit(1)
  return leftAppearance


def findParenthesisIndex (tokens):
  leftIndex = 0
  rightIndex = 0
  for index in range(len(tokens)):
    if tokens[index]['type'] == 'LEFT_PARENTHESIS':
      leftIndex = index
  for index in range(leftIndex, len(tokens)):
    if tokens[index]['type'] == 'RIGHT_PARENTHESIS':
      rightIndex = index
      break
  # error message for )(
  if rightIndex < leftIndex:
    print('Imcomplete parenthesis')
    exit(1)
  return leftIndex, rightIndex


def evaluate(tokens):
  parenthesisAppearance = countParenthesisAppearance(tokens)
  for i in range(0, parenthesisAppearance):
    # insert dummy parentheses
    tokens.insert(0, {'type': 'LEFT_PARENTHESIS'})
    tokens.append({'type': 'RIGHT_PARENTHESIS'})
    leftParenthesisIndex, rightParenthesisIndex = findParenthesisIndex(tokens)
    leftOfParenthesis = []
    insideParenthesis = []
    rightOfParenthesis = []
    for index in range(len(tokens)):
      if index < leftParenthesisIndex:
        leftOfParenthesis.append(tokens[index])
      elif index > rightParenthesisIndex:
        rightOfParenthesis.append(tokens[index])
      elif index > leftParenthesisIndex and index < rightParenthesisIndex:
        insideParenthesis.append(tokens[index])
    insideParenthesis = evalMultDiv(insideParenthesis)
    insideParenthesis = [{'type': 'NUMBER', 'number': evalAddSub(insideParenthesis)}]
    tokens = [{'type': 'PLUS'}]+leftOfParenthesis+insideParenthesis+rightOfParenthesis
  tokens = evalMultDiv(tokens)
  return evalAddSub(tokens)


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
  test("1")
  test("11")
  test("11.1")
  test("1+2")
  test("1.0+2.1-3")
  test("1*2+4*3/2")
  test("1.4/5.6+6.7*3")
  test("((4+5)+6*3)/3")
  test("(1/3)*4/2+4*(5+1)")
  test("((1.5/6)+(8/3)*9)+3")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
