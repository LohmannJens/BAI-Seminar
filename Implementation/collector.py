import tsplib95
import matplotlib.pyplot as plt
from discrete_tree_seed_algorithm import dtsa
from genetic_TSP_algortihm import gtspa

#tsp_name = "berlin52"
#tsp_name = "ch150"
#tsp_name = "tsp225"
#for tsp_name in ["berlin52", "ch150", "tsp225"]:
for tsp_name in ["eil101", "st70", "kroA100"]:

    problem = tsplib95.load(tsp_name + ".tsp")
    max_fes = 800000 # for real run
    # max_fes = 8000 # for testing purposes
    iterations = 1

    # DTSA
    for i in range(iterations):
        print("Algorithm: DTSA, Problem: "+tsp_name+", Iteration: ("+str(i)+"/"+str(iterations)+")")
        best, fes_timestamps, path_lengths = dtsa(problem, max_fes=max_fes)
        log = "[DTSA], " + str(fes_timestamps) + ", " + str(path_lengths) + ", " + str(best.path) +  ", [END]\n"
        log_file = open("logs/dtsa_" + tsp_name + ".txt", "a")
        log_file.write(log)
        log_file.close()

    # GTSPA with selection before mutation
    for i in range(iterations):
        print("Algorithm: GTSPA-SM, Problem: "+tsp_name+", Iteration: ("+str(i)+"/"+str(iterations)+")")
        best, fes_timestamps, path_lengths = gtspa(problem, pre_selection=0.25, max_fes=max_fes)
        log = "[GTSPA-SM], " + str(fes_timestamps) + ", " + str(path_lengths) + ", " + str(best.path) + ", [END]\n"
        log_file = open("logs/gtspasm_" + tsp_name + ".txt", "a")
        log_file.write(log)
        log_file.close()

    # GTSPA with selection after mutation
    for i in range(iterations):
        print("Algorithm: GTSPA-MS, Problem: "+tsp_name+", Iteration: ("+str(i)+"/"+str(iterations)+")")
        best, fes_timestamps, path_lengths = gtspa(problem, pre_selection=1, max_fes=max_fes)
        log = "[GTSPA-MS], " + str(fes_timestamps) + ", " + str(path_lengths) + ", " + str(best.path) + ", [END]\n"
        log_file = open("logs/gtspams_" + tsp_name + ".txt", "a")
        log_file.write(log)
        log_file.close()

    # GTSPA with selection before and after mutation
    for i in range(iterations):
        print("Algorithm: GTSPA-SMS, Problem: "+tsp_name+", Iteration: ("+str(i)+"/"+str(iterations)+")")
        best, fes_timestamps, path_lengths = gtspa(problem, pre_selection=0.5, max_fes=max_fes)
        log = "[GTSPA-SMS], " + str(fes_timestamps) + ", " + str(path_lengths) + ", " + str(best.path) + ", [END]\n"
        log_file = open("logs/gtspasms_" + tsp_name + ".txt", "a")
        log_file.write(log)
        log_file.close()

