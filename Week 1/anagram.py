def find_anagram(string: str, new_dict: tuple):
  string = sorted(string)
  # binary search condition
  start = 0
  mid = (len(new_dict)-1) // 2
  end = len(new_dict)-1
  for i in range(len(string)):
    if string[i] > new_dict[mid][0][i]:
      start = mid + 1
      break
    elif string[i] < new_dict[mid][0][i]:
      end = mid-1
      break
  # compare with dictionary
  for word in range(start, end):
    if string == new_dict[word][0]:
      print(new_dict[word][1])
  return None

if __name__ == '__main__':
  dictionary = open("words.txt", "r")
  new_dict = []
  for word in dictionary:
    new_dict.append((sorted(word.strip()), word.strip()))
  dictionary.close()
  new_dict = sorted(new_dict)
  randomtest = open("randomtest.txt", "r")
  for word in randomtest:
    find_anagram(word.strip(), new_dict)