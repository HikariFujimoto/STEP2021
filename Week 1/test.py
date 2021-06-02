
def countChars (string: str) -> dict:
  charCount = {}
  for char in string:
    if char in charCount.keys():
      charCount[char] += 1
    else:
      charCount[char] = 1
  return charCount


SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def count_appearance (string: str) -> list[int]:
  counter = [[0], [0]*26]
  score = 0
  for letter in string:
    alphabet_index = ord(letter)-97
    counter[1][alphabet_index] += 1
    score += SCORES[alphabet_index]
  counter[0] = score
  return counter

# create a new dict with count appearance
def create_new_dict (dictionary):
  new_dict = []
  for word in dictionary:
    new_dict.append((count_appearance(word.strip()), word.strip()))
  return new_dict

if __name__ == '__main__':
  string = "sample"
  string2 = "amplz"
  count = count_appearance(string)
  count2 = count_appearance(string2)
  for i in range(0, 25):
    if count[1][i] >= count2[1][i]:
      print(True)
    else:
      print(False)
