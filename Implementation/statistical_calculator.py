import numpy as np
import matplotlib.pyplot as plt

def get_statistical_data(filename, tsp_name):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

# Create Numpy array with final path lengths    
    final_paths = list()
    path_lengths = [line.split("], [")[2] for line in lines]
    for pl in path_lengths:
        path_lengths_sum = np.array(pl.split(", "), dtype=int)
        final_paths.append(path_lengths_sum[-1])
    final_paths_len = np.array(final_paths)

# Calculate statistical values
    mean = np.mean(final_paths_len)
    std_dev = np.std(final_paths_len)
    best_path = np.min(final_paths_len)
    worst_path = np.max(final_paths_len)
    opt_tours = {"berlin52" : 7542, "st70":675, "kroA100": 21282, "eil101": 629, "ch150" : 6528, "tsp225" : 3919}
    relative_error = np.mean((final_paths_len - opt_tours[tsp_name])/opt_tours[tsp_name] * 100)
    return [round(mean,2), round(std_dev,2), best_path, worst_path, round(relative_error,2)]

# Create Table
problems = ["berlin52", "st70", "kroA100", "eil101", "ch150" ,"tsp225"]
algorithms = ["dtsa_", "gtspasm_", "gtspams_", "gtspasms_"]
t_file = open("gen/statistical_table.tex", "w")
t_file.write("\\begin{table}[ht]\n")
t_file.write("\\caption{Statistical evaluation of the differrent algorithms for the six problems}\n")
t_file.write("\\begin{center}\n\\begin{tabular}{|c|c|c|c|c|c|c|}\n")
t_file.write("\t\\hline\n\tdataset & algorithm & mean & std. dev. & best & worst & RE(\\%)\\\\\n")
for tsp_name in problems:
    t_file.write("\t\\hline\n\t\\multirow{4}{*}{"+tsp_name+"}")
    for a in algorithms:
        data = get_statistical_data("logs/" + a + tsp_name + ".txt", tsp_name)
        t_file.write("\t\t& {} & {} & {} & {} & {} & {}\\\\\n". format(a[0:-1], data[0], data[1], data[2], data[3], data[4]))

t_file.write("\t\\hline\n\\end{tabular}\n\\end{center}\n")
t_file.write("\\label{tab:statistical_evaluation}\n\\end{table}")
t_file.close()

