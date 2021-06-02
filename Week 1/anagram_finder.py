
SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]

# create array containing appearance and score of each alphabet
def count_appearance (string: str) -> list[int]:
  counter = [0]*26
  score = 0
  for letter in string:
    alphabet_index = ord(letter)-97
    counter[alphabet_index] += 1
    score += SCORES[alphabet_index]
  counter.append(score)
  return counter

# create a new dict with count appearance
def create_new_dict (dictionary: list[str]):
  new_dict = []
  for word in dictionary:
    new_dict.append((count_appearance(word.strip()), word.strip()))
  return new_dict

def find_anagram (string:str, dictionary) -> str:
  string_count = count_appearance(string)
  anagram_index = 0
  score = 0
  # find the first anagram
  for i in dictionary:
    anagram = True
    for j in range(0, 25):
      if dictionary[i][0][j] > string_count[j]:
        anagram = False
        break
    if anagram == True:
      anagram_index = i
      score = dictionary[i][0][26]
      break
  # new condition: compare score, if larger than current score, check if anagram
  for i in range(anagram_index+1, dictionary):
    anagram = True
    if dictionary[i][0][26] > score:
      for j in range(0, 25):
        if dictionary[i][0][j] > string_count[j]:
          anagram = False
          break
      if anagram == True:
        anagram_index = i
        score = dictionary[i][0][26]
  return dictionary[anagram_index][1]

if __name__ == '__main__':
  dictionary = open("words.txt", "r")
  new_dict = create_new_dict(dictionary)
  input = open("medium.txt", "r")
  file = open("mediumresult.txt", "w")
  for word in input:
    file.write(find_anagram(word.strip(), new_dict) + "\n")
  dictionary.close()
  file.close()