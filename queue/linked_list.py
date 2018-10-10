"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)

    if not self.head:
      self.head = new_node
    else:
      self.tail.set_next(new_node)

    self.tail = new_node

  def remove_head(self):
    old_head = self.head

    if old_head:
      self.head = old_head.get_next()
      if not self.head:
        self.tail = None 
    
    return old_head.get_value() if hasattr(old_head, 'get_value') else old_head

  def contains(self, value, node=False):
    if node == False:
      node = self.head

    if node != None:
      if value == node.get_value():
        return True
      else:
        return self.contains(value, node.get_next())
    else:
      return False

  def get_max(self):
    maximum = None
    current_node = self.head

    while current_node:
      current_val = current_node.get_value()
      maximum = current_val if maximum == None or current_val > maximum else maximum
      current_node = current_node.get_next()
    
    return maximum
