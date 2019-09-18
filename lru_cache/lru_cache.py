from dll_queue import Queue

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = 0
    self.queue = Queue()
    self.storage = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    pass

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if self.queue.len() == 10:
        del self.storage[self.queue.dequeue()]
    if key in self.storage:
        self.storage[key] = value
    self.storage[key] = value
    print(self.storage)
    self.queue.enqueue(key)
    print(self.queue.len())
    print(self.queue.len())
    print(self.storage)
   
testCache = LRUCache()

testCache.set(1, 1)




# Testing a new method of adding comments to a python file without breaking it
# First we need to get the storage (dict) working, then we get the queue working, then we start logic to add things to the queue and dict

# We have the que and storage working set

# Next step: If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room.

# Something like if self.queue.len() is probably 10, maybe 9 who knows, self.queue.dequeue()

# There's something in the spec about a limit of 10, I don't know why thats there, when the queue data structure already has a list that I'm using to check how many items are in the queue.

# Done probably, we'll see
# Don't have a way to see whats in my queue, but it's probably working
# Need to remove the element that got pushed out of the queue, from the dictionary as well
