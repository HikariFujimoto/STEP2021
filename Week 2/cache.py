import sys

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library (e.g., collections.OrderedDict).
#       Implement the data structure yourself.
class Cache:
  # Initializes the cache.
  # |n|: The size of the cache.
  def __init__(self, n):
    ###########################
    # Write your code here :) #
    ###########################
    self.dict:dict[Page, LinkedListNode] = {}
    self.maxsize = n
    self.linked_list = LinkedList()

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # |url|: The accessed URL
  # |contents|: The contents of the URL
  def access_page(self, url, contents):
    ###########################
    # Write your code here :) #
    ###########################
    page = Page(url, contents)
    # check whether page exists in dict or not
    # if existing
    if page in self.dict:
      # reconnect the prev and next nodes
      self.linked_list.remove_node(self.dict[page])
      # connect page to beginning
      self.linked_list.prepend_node(self.dict[page])
    # if not existing
    else:
      node = LinkedListNode(page) 
      # add to dict, connect page to beginning, delete last node if size > maxsize
      self.dict[page] = node
      self.linked_list.prepend_node(node)
      if len(self.dict) > self.maxsize:
        deleted_node = self.linked_list.remove_last_node()
        del self.dict[deleted_node.value]

  # Return the URLs stored in the cache. The URLs are ordered
  # in the order in which the URLs are mostly recently accessed.
  def get_pages(self):
    ###########################
    # Write your code here :) #
    ###########################
    page_list = self.linked_list.getValues()
    for i in range(len(page_list)):
      page_list[i] = page_list[i].url
    return page_list

class LinkedListNode: # each element of LinkedList class
  def __init__(self, value):
    self.prev = None
    self.next = None
    self.value = value

class LinkedList:
  def __init__(self):
    # need to know first and last node
    self.first:LinkedListNode = None
    self.last:LinkedListNode = None
  
  def prepend_node(self, node:LinkedListNode): # add to the beggining
    node.prev = None
    node.next = self.first
    self.first = node

  def remove_node(self, node:LinkedListNode):
    if self.first == node:
      self.remove_first_node()
      return
    if self.last == node:
      self.remove_last_node()
      return
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

  def remove_first_node(self):
    deleted_node = self.first
    if self.first == self.last:
      self.first = None
      self.last = None
    else:
      next_node = self.first.next
      self.first.next = None
      next_node.prev = None
      self.first = next_node
    return deleted_node

  def remove_last_node(self):
    deleted_node = self.last
    if self.first == self.last: # if linked list with only one node
      self.first = None
      self.last = None
    else:
      node = self.last.prev
      self.last.prev = None
      node.next = None
      self.last = node
    return deleted_node

  def getValues(self):
    values = []
    node = self.first
    while node:
      values.append(node.value)
      node = node.next
    return values

class Page:
  def __init__(self, url, contents):
    self.url = url
    self.contents = contents
  
  def __hash__(self):
    return hash(self.url)

# Does your code pass all test cases? :)
def cache_test():
  # Set the size of the cache to 4.
  cache = Cache(4)
  # Initially, no page is cached.
  equal(cache.get_pages(), [])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # "a.com" is cached.
  equal(cache.get_pages(), ["a.com"])
  # Access "b.com".
  cache.access_page("b.com", "BBB")
  # The cache is updated to:
  #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["b.com", "a.com"])
  # Access "c.com".
  cache.access_page("c.com", "CCC")
  # The cache is updated to:
  #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
  # Access "d.com".
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "d.com" again.
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "a.com" again.
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
  cache.access_page("c.com", "CCC")
  equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is full, so we need to remove the least recently accessed page "b.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
  # Access "f.com".
  cache.access_page("f.com", "FFF")
  # The cache is full, so we need to remove the least recently accessed page "c.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "f.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "f.com", "a.com", "c.com"])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "e.com", "f.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "e.com", "f.com", "c.com"])
  print("OK!")

# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
  assert(list1 == list2)

if __name__ == "__main__":
  cache_test()