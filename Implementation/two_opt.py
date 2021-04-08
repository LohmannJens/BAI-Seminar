import numpy as np
import tsplib95
from TSPHelper import calc_length
from TSPTree import TSPTree



def two_opt(tree):
    path = tree.path
    problem = tree.problem
    
    def two_opt_swap(i, j):
        new_path = path.copy()
        new_path[i:j] = path[j-1:i-1:-1]
        return new_path
        
    improved = True
    while improved:
      improved = False
      for i in range(1, len(path)):
        for j in range(i+1, len(path)+1):
          new_path = two_opt_swap(i,j)
          if calc_length(problem, new_path) < calc_length(problem, path):
            path = new_path
            improved = True
    return TSPTree(problem, path)
