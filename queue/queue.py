import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    return self.storage.add_to_tail(item)
  
  def dequeue(self):
    remove_result = self.storage.remove_head()
    if remove_result != None:
      self.size -= 1
    return remove_result
    
  def len(self):
    return self.size
    
