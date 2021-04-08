import numpy as np
import matplotlib.pyplot as plt
import tsplib95
import plotTSP

opt_tours = {"berlin52" : 7542, "st70":675, "kroA100": 21282, "eil101": 629, "ch150" : 6528, "tsp225" : 3919}

def get_final_paths(filename, tsp_name):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    
    final_path_len = list()
    path_lengths = [line.split("], [")[2] for line in lines]
    for pl in path_lengths:
        path_lengths_sum = np.array(pl.split(", "), dtype=int)
        final_path_len.append(path_lengths_sum[-1])
    return np.array(final_path_len)

for tsp_name in ["berlin52", "ch150", "tsp225", "eil101", "st70", "kroA100"]:
    fig, ax = plt.subplots()
    # Plot optimum path length as horizontal red line
    optimum = opt_tours[tsp_name]
    ax.axhline(y=optimum, color='red')
    # make the boxplots
    algorithms = ["dtsa", "gtspasm", "gtspams", "gtspasms"]
    optimal = tsplib95.load("opt_tours/" + tsp_name + ".opt.tour" )
    data = list()
    for a in algorithms:
        data.append(get_final_paths("logs/" + a + "_" + tsp_name + ".txt",tsp_name))
    ax.boxplot(data, labels = algorithms)
    ax.set_ylabel("path length")
    fig.savefig("gen/boxplot_"+ tsp_name +".pdf")
