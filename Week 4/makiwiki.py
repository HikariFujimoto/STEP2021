import sys

def file_open():
    pages = {}
    links = {}

    with open('data/pages.txt', encoding="utf-8") as f:
      for data in f.read().splitlines():
        page = data.split('\t')
        # page[0]: id, page[1]: title
        pages[page[0]] = page[1]

    with open('data/links.txt', encoding="utf-8") as f:
      for data in f.read().splitlines():
        link = data.split('\t')
        # link[0]: id (from), links[1]: id (to)
        if link[0] in links:
          links[link[0]].append(int(link[1]))
        else:
          links[link[0]] = [int(link[1])]
    return pages, links

def neighbors_in(links,k):
    neighbors = []
    for key, value in links.items():
        if key == k:
            neighbors = list(value)
            break
    return neighbors

def main():
  (pages,links) = file_open()
  queue = []
  new_neighbors = []
  already_seen = set()
  goal = '渋谷'

  for k, v in pages.items():
    if v == 'Google':
      print('Google',k)
      break

  new_neighbors = neighbors_in(links,k)

  item = new_neighbors[0]

  queue = new_neighbors.copy()
  if str(item) == goal:
      print(goal)
      sys.exit()
  else:
      already_seen.add(item)
      del queue[0]

  new_neighbors += neighbors_in(links,item)

  while len(queue) > 0:
      item = new_neighbors[0]

      if item in already_seen:
          del new_neighbors[0]
      else:
          queue = new_neighbors.copy()
          if str(item) == goal:
              print(goal)
              exit()
          else:
              already_seen.add(item)
              del queue[0]
              del new_neighbors[0]

      new_neighbors += neighbors_in(links,str(item))



if __name__ == '__main__':
    main()