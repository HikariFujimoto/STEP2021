import math
from common import print_tour, read_input

def find_distance(city1, city2) -> float:
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_total_distance(path, dist):
  total_dist = 0.0
  for index in range(0, len(path)-1):
    total_dist += dist[path[index]][path[index+1]]
  total_dist += dist[path[-1]][path[0]]
  return total_dist 

def find_insertion_index(current_city: int, path: list[int], dist: list[list[float]]) -> int:
  insertion_index = 0
  min_dist = 1000000.0
  for i in range(len(path)):
    node1 = path[i-1]
    node2 = path[i]
    dist_after_insetion = dist[current_city][node1] + dist[current_city][node2] - dist[node1][node2]
    if dist_after_insetion < min_dist:
      min_dist = dist_after_insetion
      insertion_index = i
  return insertion_index

def nearest_insertion(input_data):
  N = len(input_data)

  # calculate distance between each nodes
  dist = [[0.0] * N for i in range(N)]
  for i in range(N):
    for j in range(i, N):
      dist[i][j] = dist[j][i] = find_distance(input_data[i], input_data[j])

  # initialize with two nodes
  current_city = 0
  unvisited_cities = set(range(0, N))
  unvisited_cities.remove(current_city)
  path = [current_city]
  next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
  unvisited_cities.remove(next_city)
  path.append(next_city)
  current_city = next_city
  
  # continue insertion until no unvisited cities are left
  while unvisited_cities:
    next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
    unvisited_cities.remove(next_city)
    insertion_index = find_insertion_index(next_city, path, dist)
    path.insert(insertion_index, next_city)
    current_city = next_city
  return path, find_total_distance(path, dist)
  
def get_challenge_num ():
  challenge_num = input('Please input challenge No.:')
  if int(challenge_num) > 7:
    print("Number out of range")
    exit(-1)
  input_file_name = "input_" + challenge_num + ".csv"
  output_file_name = "output_" + challenge_num + ".csv"
  return input_file_name, output_file_name 

def write_output (path: list[int], output_file_name: str):
  output = open(output_file_name, "w")
  output.write("index\n")
  for node in path:
    output.write(str(node) + "\n")
  output.close

if __name__ == '__main__':
  input_file_name, output_file_name = get_challenge_num()
  input_data = read_input(input_file_name)
  path, total_dist = nearest_insertion(input_data)
  write_output(path, output_file_name)
  print_tour(path)
  print("Total Distance:", total_dist)