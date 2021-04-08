import numpy as np
import matplotlib.pyplot as plt
import tsplib95
import plotTSP

def get_best_path(filename, tsp_name):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    
    final_path_len = list()
    path_lengths = [line.split("], [")[2] for line in lines]
    for pl in path_lengths:
        path_lengths_sum = np.array(pl.split(", "), dtype=int)
        final_path_len.append(path_lengths_sum[-1])
    final_path_indices = [line.split("], [")[3] for line in lines]
    best_path = final_path_indices[final_path_len.index(min(final_path_len))]
    return np.array(best_path.split(", "), dtype=int)

for tsp_name in ["berlin52", "ch150", "tsp225", "eil101", "st70", "kroA100"]:
    # Plot best path
    problem = tsplib95.load(tsp_name + ".tsp")
    algorithms = ["dtsa_", "gtspasm_", "gtspams_", "gtspasms_"]
    optimal = tsplib95.load("opt_tours/" + tsp_name + ".opt.tour" )
    for a in algorithms:
        best_path = get_best_path("logs/" + a + tsp_name + ".txt",tsp_name)
        plotTSP.plotTSP(problem, [best_path], "gen/best_path_" + a + tsp_name + ".pdf")

    plotTSP.plotTSP(problem, [optimal.tours[0]], "gen/optimal_path_" + tsp_name + ".pdf")
