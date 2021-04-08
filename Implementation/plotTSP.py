import numpy as np
import tsplib95
import matplotlib.pyplot as plt

def get_coordinates(paths, problem):
    x = list()
    y = list()
    if paths is None:
        x = list(p[0] for p in problem.node_coords.values())
        y = list(p[1] for p in problem.node_coords.values())
        return x,y
    else:
        for path in paths:
            first = path[0]
            for node in path:
                point = problem.node_coords[node]
                x.append(point[0])
                y.append(point[1])
            point = problem.node_coords[first]
            x.append(point[0])
            y.append(point[1])
            yield x,y

def plotTSP(problem, paths=None, filename=""):
    plt.clf()
    data =list()
    colors = ["red", "blue"]
    if paths is not None:
        for x,y in get_coordinates(paths, problem):
            data.append((x,y))
        for d, color in zip(data,colors):
            plt.plot(d[0], d[1], color)
    plt.scatter(data[0][0],data[0][1])
    if filename != "":
        plt.savefig(filename)
    else:
        plt.show()

