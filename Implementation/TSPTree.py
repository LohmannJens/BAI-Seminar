import numpy as np
import tsplib95
import matplotlib.pyplot as plt

class TSPTree:
  def __init__(self, problem, path=None):
    self.problem = problem
    n_vertices = list(problem.get_nodes())
    self.d_cities = len(n_vertices)
    if path is not None:
      self.path = path
    else:
      self.path = np.random.permutation(n_vertices)

  def calc_length(self):
    length = 0
    temp_node = self.path[-1]
    for node in self.path:
      length += self.problem.get_weight(temp_node,node)
      temp_node = node
    return length

  def copy(self):
    return TSPTree(self.problem, self.path.copy())

  def get_swap_seed(self):
    seed = self.copy()
    first = np.random.randint(0,self.d_cities)
    second = np.random.randint(0,self.d_cities)
    seed.swap(first, second)
    return seed

  def swap(self, first_index: int, second_index: int):
    path = self.path
    first = path[first_index]
    second = path[second_index]
    path[first_index] = second
    path[second_index] = first
    return path

  def get_shift_seed(self):
    seed = self.copy()
    first = np.random.randint(0,self.d_cities)
    second = np.random.randint(0,self.d_cities)
    seed.shift(first, second)
    return seed

  def shift(self, first_index: int, second_index: int):
    path = self.path
    path_length = len(path)
    first = path[first_index]
    i = first_index
    while i != second_index:
      path[i] = path[(i+1)%path_length]
      i = (i+1)%path_length
    path[second_index] = first
    return path

  def get_symmetry_seed(self):
    seed = self.copy()
    first = np.random.randint(0,self.d_cities)
    second = np.random.randint(0,self.d_cities)
    if first > second:
      seed.symmetry(second, first)
    else:
      seed.symmetry(first, second)
    return seed

  def symmetry(self, first_index, second_index):
    path = self.path
    while first_index < second_index:
      # simply swap first and last node
      self.swap(first_index, second_index)
      # until the indeces meet in the middle
      first_index += 1
      second_index -= 1
    return path
