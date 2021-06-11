import math
from common import print_tour, read_input
from collections import deque

def find_distance(city1, city2) -> float:
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(path, input):
  total_dist = 0.0
  for index in range(len(path)):
    total_dist += find_distance(input[index-1], input[index])
  return total_dist

def two_opt(path, input):
  best = path
  improved = True
  while improved:
    improved = False
    for i in range(1, len(path)-2):
      for j in range(i+1, len(path)):
        if j-1 == 1: continue
        new_route = path[:]
        new_route[i:j] = path[j-1:i-1:-1]
        if total_distance(new_route, input) < total_distance(path, input):
          best = new_route
          improved = True
    path = best
  return best

def greedy_algorithm(input):
  N = len(input)

  dist = [[0.0] * N for i in range(N)]
  for i in range(N):
    for j in range(i, N):
      dist[i][j] = dist[j][i] = find_distance(input[i], input[j])

  current_city = 0
  unvisited_cities = set(range(1, N))
  path = [current_city]

  while unvisited_cities:
    next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
    unvisited_cities.remove(next_city)
    path.append(next_city)
    current_city = next_city
  return path

def write_output (path: list[int]):
  output = open("output_3.csv", "w")
  output.write("index\n")
  for node in path:
    output.write(str(node) + "\n")
  output.close

if __name__ == '__main__':
  input = read_input("input_3.csv")
  path = greedy_algorithm(input)
  path = two_opt(path, input)
  write_output(path)
  print_tour(path)


