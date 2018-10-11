from math import floor, inf

class Heap:
  """
  Formulas!
  l = 2i + 1
  r = 21 + 2
  p = floor((i-2)/2)
  """

  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    i = len(self.storage) - 1
    self._bubble_up(i)

  def delete(self):
    deleted_node = self.storage.pop(0)
    self._sift_down(0)
    return deleted_node

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    print('new bubble @ index:', index)

    p = floor((index - 2)/ 2) if index > 1 else 0
    # values
    child = self.storage[index]
    parent = self.storage[p]
    print('bubble up - index:', index, 'p index:', p)
    print('child:', child, 'parent:', parent)
    if child > parent:
      self.storage[p] = child
      self.storage[index] = parent
      self._bubble_up(p)

  def _sift_down(self, index):
    print('another sift down at index:', index)
    def swap_in_storage(i1, i2, lst=self.storage):
      temp = lst[i1]
      lst[i1] = lst[i2]
      lst[i2] = temp

    # indices
    left_i = 2 * index + 1
    right_i = 2 * index + 2
    max_i = self.get_size() - 1

    if index > max_i:
      return

    # values
    root = self.storage[index]
    left = self.storage[left_i] if left_i <= max_i else -inf
    right = self.storage[right_i] if right_i <= max_i else -inf
    print('root:', root, 'left:', left, 'right:', right)


    if root < left and root < right:
      if left > right:
        swap_in_storage(index, left_i)
        self._sift_down(left_i)
      else:
        swap_in_storage(index, right_i)
        self._sift_down(right_i)
    elif root < left:
      swap_in_storage(index, left_i)
      self._sift_down(left_i)
    elif root < right:
      swap_in_storage(index, right_i)
      self._sift_down(right_i)
    