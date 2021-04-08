#!/usr/bin/env python3
import TSPTree
import tsplib95
import numpy as np
from two_opt import two_opt
import TSPHelper

def gtspa(problem, n_trees=0, pre_selection=0.5, max_fes=800000):
  # PARAMETERS
  fes = 0 #function evaluation number
  max_fes = max_fes # paper proposed 800000 for dtsa
                    # we also used 800000 here to keep the number
                    # of evaluated functions similar
  cities = list(problem.get_nodes())
  if n_trees==0:
    n_trees = len(cities) # paper proposed n_trees = d_cities for dtsa
  pre_selection = max(0.25, pre_selection)   # should be between 0.25 and 1
  pre_selection = min(1, pre_selection)      # if pre_selection = 1,
  k_survivers = int(pre_selection * n_trees) # there is no selection before mutation

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

  # do the main stuff
  while fes <= max_fes:
    # print the percentage and current best tree just for convinience
    best = TSPHelper.find_best(trees) 
    if len(best.path) < len(cities):
      print("ERROR!")
    percentage = int((fes / max_fes) * 100)
    best_path_length = best.calc_length()
    print("["+str(percentage)+"%] - best of all trees: " + str(best_path_length))

    # save data to plot convergence later
    fes_timestamps.append(fes)
    best_path_lengths.append(best_path_length)

    next_trees = list()
    # determine the best k trees to survive via using the objective function values
    best_k_trees = n_trees
    if k_survivers < n_trees:
      best_k_trees = TSPHelper.find_n_best(trees, k_survivers)
    else:
      best_k_trees = trees

    # calculate seeds for current tree and add them to next generation
    for tree in best_k_trees:
      next_trees.append(tree)
      next_trees.append(tree.get_swap_seed())
      next_trees.append(tree.get_shift_seed())
      next_trees.append(tree.get_symmetry_seed())
      fes += 3

    # prepare for next iteration
    if n_trees < len(next_trees):
      trees = TSPHelper.find_n_best(next_trees, n_trees)
    else:
      trees = next_trees

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
