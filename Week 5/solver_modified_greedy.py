import math
import random
from common import print_tour, read_input
from collections import deque

def find_distance(city1, city2) -> float:
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(path, input):
  total_dist = 0.0
  for index in range(len(path)):
    total_dist += find_distance(input[path[index-1]], input[path[index]])
  return total_dist

def two_opt(path, input):
  best = path
  for i in range(1, len(path)-2):
    for j in range(i+1, len(path)):
      if j-1 == 1: continue
      new_route = path[:]
      new_route[i:j] = path[j-1:i-1:-1]
      if total_distance(new_route, input) < total_distance(path, input):
        best = new_route
  return best

def greedy_algorithm(input):
  N = len(input)

  dist = [[0.0] * N for i in range(N)]
  for i in range(N):
    for j in range(i, N):
      dist[i][j] = dist[j][i] = find_distance(input[i], input[j])

  best_path = []
  best_dist = 1000000
  for i in range(0, 5):
    current_city = random.randint(0, N-1)
    print("Trial No.", i+1, "Starting from node:", current_city)
    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(current_city)
    path = [current_city]

    while unvisited_cities:
      next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
      unvisited_cities.remove(next_city)
      path.append(next_city)
      current_city = next_city
    path = two_opt(path, input)
    if total_distance(path, input) < best_dist:
      best_path = path
  return best_path

def write_output (path: list[int]):
  output = open("output_6.csv", "w")
  output.write("index\n")
  for node in path:
    output.write(str(node) + "\n")
  output.close

if __name__ == '__main__':
  input = read_input("input_6.csv")
  path = greedy_algorithm(input)
  write_output(path)
  print_tour(path)