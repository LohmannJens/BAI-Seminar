#!/usr/bin/env python3
import TSPTree
import tsplib95
import numpy as np
import matplotlib.pyplot as plt
from two_opt import two_opt
import TSPHelper

def dtsa(problem, n_trees=0, search_tendency=0.5, max_fes=800000):
  # PARAMETERS
  fes = 0 #function evaluation number
  max_fes = max_fes # paper proposed 800000
  cities = list(problem.get_nodes())
  if n_trees==0:
    n_trees = len(cities) # paper proposed n_trees = d_cities
  search_tendency = search_tendency # must be between 0 and 1 # paper proposed 0.5

  # INITIALIZATION
  trees = list()
  # first tree is determined via a nearest neighbor tour
  first_tree = TSPTree.TSPTree(problem)
  first_tree.path = TSPHelper.get_nearest_neighbor_tour(problem)
  trees.append(first_tree)
  for i in range(n_trees-1):
    tree = TSPTree.TSPTree(problem)
    trees.append(tree)
  fes = n_trees

  # variables for convergence plot
  fes_timestamps = list()
  best_path_lengths = list()

  # THE ALGORITHM
  # do the main stuff
  while fes <= max_fes:
    # determine the best tree via using the objective function values
    best = TSPHelper.find_best(trees)
    # print the percentage and current best tree just for convinience
    percentage = int((fes / max_fes) * 100)
    best_path_length = best.calc_length()
    print("["+str(percentage)+"%] - best of all trees: " + str(best_path_length))

    # save data to plot convergence later
    fes_timestamps.append(fes)
    best_path_lengths.append(best_path_length)

    next_trees = list()
    for tree in trees:
      # calculate seeds for current tree
      random_tree = trees[np.random.randint(0,n_trees)]
      rand = np.random.random()
      seeds = list()
      if (rand < search_tendency):
        seeds.append(best.get_swap_seed())
        seeds.append(best.get_shift_seed())
        seeds.append(best.get_symmetry_seed())
      else:
        seeds.append(tree.get_swap_seed())
        seeds.append(tree.get_shift_seed())
        seeds.append(tree.get_symmetry_seed())
      seeds.append(random_tree.get_swap_seed())
      seeds.append(random_tree.get_shift_seed())
      seeds.append(random_tree.get_symmetry_seed())
      fes += 6

      # determine best seed
      seeds.append(tree)
      best_seed = TSPHelper.find_best(seeds)
      if len(best_seed.path) < len(cities):
        print("ERROR!")
      next_trees.append(best_seed)

    # prepare for next iteration
    trees = next_trees

  # FINAL OPTIMIZATION
  # best tree after while loop
  best = TSPHelper.find_best(trees)
  print("best tree after while loop: " + str(best.calc_length()))
  # do optimization with 2-opt
  best = two_opt(best)
  best_path_length = best.calc_length()
  print("best tour after 2-opt: " + str(best_path_length))

  # add final path data to convergence data
  fes_timestamps.append(fes)
  best_path_lengths.append(best_path_length)

  # RETURN BEST
  return best, fes_timestamps, best_path_lengths
