from common import print_tour, read_input
import math

def get_challenge_num ():
  challenge_num = input('Please input challenge No.:')
  input_file_name = "input_" + challenge_num + ".csv"
  output_file_name = "output_" + challenge_num + ".csv"
  return input_file_name, output_file_name 

def find_distance(city1, city2) -> float:
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def get_total_distance(path, dist):
  total_dist = 0.0
  for i in range(0, len(path)-1):
    total_dist += dist[i][i+1]
  total_dist += dist[-1][0]
  return total_dist 

if __name__ == "__main__":
  path = [4, 3, 2, 1, 0]
  data = read_input("input_0.csv")
  N = len(data)  
  dist = [[0.0] * N for i in range(N)]
  for i in range(N):
    for j in range(i, N):
      dist[i][j] = dist[j][i] = find_distance(data[i], data[j])
  
  print(get_total_distance(path, dist))