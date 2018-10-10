# import sys
# sys.path.append('../linked_list')
# print(sys.path)
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    result = self.storage.remove_head()
    
    if result:
      self.size -= 1

    return result

  def len(self):
    return self.size
