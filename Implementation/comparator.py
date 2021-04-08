import tsplib95
import matplotlib.pyplot as plt
from discrete_tree_seed_algorithm import dtsa
from genetic_TSP_algortihm import gtspa

#problem_name = "berlin52"
problem_name = "ch150"
#problem_name = "tsp225"

problem = tsplib95.load(problem_name + ".tsp")
max_fes = 800000

plt.clf()
plt.title("convergence comparison")

# DTSA
best, fes_timestamps, best_path_lengths = dtsa(problem, max_fes=max_fes)
plt.plot(fes_timestamps, best_path_lengths, label="DTSA")

# GTSPA with selection before mutation
best, fes_timestamps, best_path_lengths = gtspa(problem, pre_selection=0.25, max_fes=max_fes)
plt.plot(fes_timestamps, best_path_lengths, label="GTSPA-SM")

# GTSPA with selection after mutation
best, fes_timestamps, best_path_lengths = gtspa(problem, pre_selection=1, max_fes=max_fes)
plt.plot(fes_timestamps, best_path_lengths, label="GTSPA-MS")

# GTSPA with selection before and after mutation
best, fes_timestamps, best_path_lengths = gtspa(problem, pre_selection=0.5, max_fes=max_fes)
plt.plot(fes_timestamps, best_path_lengths, label="GTSPA-SMS")

plt.legend()
plt.savefig("gen/convergence_" + problem_name + ".pdf")
