SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]

# create array containing score and appearance of each alphabet
def count_appearance (string: str) -> list[list[int]]:
  counter = [[0], [0]*26]
  score = 0
  for letter in string:
    alphabet_index = ord(letter)-97
    counter[1][alphabet_index] += 1
    score += SCORES[alphabet_index]
  counter[0] = score
  return counter

# create a new dict with count appearance
def create_new_dict (dictionary: list[str]):
  new_dict = []
  for word in dictionary:
    new_dict.append((count_appearance(word.strip()), word.strip()))
  return sorted(new_dict)

def find_anagram (string:str, dictionary) -> str:
  string_count = count_appearance(string)
  anagram_index = 0
  for i in range(len(dictionary)-1, 0, -1):
    is_anagram = True
    for j in range(0, 26):
      if dictionary[i][0][1][j] > string_count[1][j]:
        is_anagram = False
        break
    if is_anagram: #if is_anagram(dictionary, string_count)
      anagram_index = i
      break
  return dictionary[anagram_index][1]

if __name__ == '__main__':
  dictionary = open("words.txt", "r")
  new_dict = create_new_dict(dictionary)
  #change the input and file name to medium/large
  input = open("small.txt", "r")
  file = open("smallresult.txt", "w")
  for word in input:
    file.write(find_anagram(word.strip(), new_dict) + "\n")
  dictionary.close()
  file.close()