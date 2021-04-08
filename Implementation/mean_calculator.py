import numpy as np
import matplotlib.pyplot as plt

def get_mean_data(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    n = len(lines)

    timestamps_str = lines[0].split("], [")[1] # should be the same for every log so I am taking the first
    timestamps = np.array(timestamps_str.split(", "), dtype=int)
    path_lengths_str = [line.split("], [")[2] for line in lines]
    path_lengths = [np.array(pl.split(", "), dtype=int) for pl in path_lengths_str]
    path_lengths_sum = sum(pl for pl in path_lengths)
    path_lengths_mean = path_lengths_sum / n
    path_lengths_std = np.array([np.std( [pl[i] for pl in path_lengths] ) for i in range(len(timestamps))])
    sigma_interval = 1.64 * path_lengths_std
    return timestamps, path_lengths_mean, sigma_interval

for tsp_name in ["berlin52", "ch150", "tsp225", "eil101", "st70", "kroA100"]:
    # Create Plot
    fig, ax = plt.subplots()

    # DTSA
    timestamps, path_lengths_mean, si = get_mean_data("logs/dtsa_"+tsp_name+".txt")
    ax.plot(timestamps, path_lengths_mean, label="DTSA")
    #ax.fill_between(timestamps, (path_lengths_mean-si), (path_lengths_mean+si), alpha=.2)

    # GTSPA-SM
    timestamps, path_lengths_mean, si = get_mean_data("logs/gtspasm_"+tsp_name+".txt")
    ax.plot(timestamps, path_lengths_mean, label="GTSPA-SM")
    #ax.fill_between(timestamps, (path_lengths_mean-si), (path_lengths_mean+si), alpha=.2)

    # GTSPA-MS
    timestamps, path_lengths_mean, si = get_mean_data("logs/gtspams_"+tsp_name+".txt")
    ax.plot(timestamps, path_lengths_mean, label="GTSPA-MS")
    #ax.fill_between(timestamps, (path_lengths_mean-si), (path_lengths_mean+si), alpha=.2)

    # GTSPA-SMS
    timestamps, path_lengths_mean, si = get_mean_data("logs/gtspasms_"+tsp_name+".txt")
    ax.plot(timestamps, path_lengths_mean, label="GTSPA-SMS")
    #ax.fill_between(timestamps, (path_lengths_mean-si), (path_lengths_mean+si), alpha=.2)

    ax.legend()
    ax.set_xlabel("steps")
    ax.set_ylabel("path length")
    fig.savefig("gen/mean_convergence_"+tsp_name+".pdf")
