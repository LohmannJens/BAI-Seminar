import numpy as np

def find_best(trees):
  best_tree = trees[0]
  min_length = best_tree.calc_length()
  for tree in trees:
    length = tree.calc_length()
    if length < min_length:
      best_tree = tree
      min_length = length
  return best_tree

def find_n_best(trees, n=1):
  # work on a copy and sort by path length
  sorted_trees = trees.copy()
  sorted_trees.sort(key=lambda t: t.calc_length())
  return sorted_trees[:n]

def calc_length(problem, path):
    length = 0
    temp_node = path[-1]
    for node in path:
        length += problem.get_weight(temp_node,node)
        temp_node = node
    return length

def get_nearest_neighbor_tour(problem):
    nodes = list(problem.get_nodes())
    first_node = np.random.randint(1, len(nodes)+1)
    path = [first_node]
    nodes.remove(first_node)
    
    def get_nearest_neighbor(start_node):
        best = nodes[0]
        best_weight = problem.get_weight(start_node, nodes[0])
        for n in nodes:
            if problem.get_weight(start_node, n) < best_weight:
                best = n
                best_weight = problem.get_weight(start_node, n)
        return best
    
    while len(nodes) > 0:
        new_neighbor = get_nearest_neighbor(path[-1])
        path.append(new_neighbor)
        nodes.remove(new_neighbor)
    return path

