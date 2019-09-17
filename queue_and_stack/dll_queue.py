import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []

  def enqueue(self, value):
    DoublyLinkedList.move_to_end(self, 1)
  
  def dequeue(self):
    DoublyLinkedList.remove_from_head(self)

  def len(self):
    len(self.storage)
