import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.root = None
    self.currentRoot = None
  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert

  # After creating a node we need to find out how to traverse the tree
  # How do I know if I'm at the root of a tree?
  # What is the root of a binary search tree really?
  # Does it have 0,1, or 2 branches. A tree can only have one root and two branches
  # But we don't know for example, if a root has one branch, we don't know if we should insert there. For example, we have (this is hard to describe on text), but a tree of 3-(l)2-(r)5 and we want to insert 4. So we start at three, four is greater than 3, so we go to five. Four is less than five, so we'll insert it there, unless, there's another element there.
  def insert(self, value):
    # covers the first branch
    if self.root == None:
        value = self.root
        
    if value < self.root:
        value = self.left
    if value >= self.root:
        value = self.right
        

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children

  def contains(self, target):
    pass

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    pass

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 

  def for_each(self, cb):
    pass
