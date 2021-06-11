from collections import deque

def read_file():
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
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}
  return pages, links

def find_id(pages: dict[str, str], name: str) -> str:
  for k, v in pages.items():
    if v == name:
      return k
  raise Exception ("Item not found")

def find_path(child_node: str, connection: dict[str, str]) -> list[str]:
  # recursion to return string list of path taken
  if connection[child_node] == 'root_node':
    return [child_node]
  else:
    path = find_path(connection[child_node], connection)
    path.append(child_node)
    return path

def print_path(path: list[str], pages: dict[str, str]):
  for nodes in path:
    print(pages[nodes], "(ID:",nodes,")")
  return None

def bfs(links: dict[str, set[str]], root_node: str, target_node: str) -> list[str]:
  queue = deque()
  queue.append(root_node)
  visited = {}
  visited[root_node] = 'root_node'
  while queue:
    if queue[0] != target_node:
      # add adjacent nodes of queue[0] that is not in visited, into queue and visited
      if queue[0] in links:
        for adjacent_node in links[queue[0]]:
          if adjacent_node not in visited:
            queue.append(adjacent_node)
            visited[adjacent_node] = queue[0]
      queue.popleft()
    else: # when queue == target_node
      return find_path(target_node, visited)
  raise Exception("Path not found")

if __name__ == '__main__':
  pages, links = read_file()
  root_node = 'Google'
  target_node = '渋谷'
  path = bfs(links, find_id(pages, root_node), find_id(pages, target_node))
  print("Path from", root_node, "->", target_node)
  print_path(path, pages)

