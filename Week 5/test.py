import math
from common import print_tour, read_input


def check_intercection(input, city_index1, city_index2, city_index3, city_index4) -> bool:
  city1 = input[city_index1]
  city2 = input[city_index2]
  city3 = input[city_index3]
  city4 = input[city_index4]
  interval = [max( min(city1[0], city2[0]), min(city3[0], city4[0])), min( max(city1[0], city2[0]), max(city3[0], city4[0]))]
  if (max(city1[0], city2[0]) < min(city3[0], city4[0])):
    return False # interval of segments does not exist
  A1 = (city1[1] - city2[1]) / (city1[0] - city2[0])
  A2 = (city3[1] - city4[1]) / (city3[0] - city4[0])
  b1 = city1[1] - A1*city1[0]
  b2 = city3[1] - A2*city3[0]
  if (A1 == A2):
    return False # segments are parallel
  Xa = (b2 - b1) / (A1 - A2)
  if (Xa < interval[0] or Xa > interval[1]):
    return False # intersection out of segments
  else: 
    return True


  # while unvisited_cities:
  #   next_node = 0
  #   min_dist = 0
  #   for index in unvisited_cities:
  #     for city in range(1, len(path)):
  #       if check_intercection(input, path[city-1], path[city], current_city, index) == False:
  #         if min_dist == 0 or dist[index][city] < min_dist:
  #           next_node = index
  #           min_dist = dist[index][city]
  #     if next_node == 0:
  #       next_node = min(unvisited_cities, key=lambda city: dist[current_city][city])
  #   unvisited_cities.remove(next_node)
  #   current_city = next_node
  #   path.append(next_node)
  # return path

def find_distance(city1, city2) -> float:
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


if __name__ == '__main__':
  input = read_input("input_0.csv")
  dist = []
  for i in range(len(input)):
    for j in range(i+1, len(input)):
      dist.append((find_distance(input[j], input[i]), i, j))
  dist = sorted(dist)
  print(dist)