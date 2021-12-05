import pandas as pd
import numpy as np
from collections import Counter
import itertools

### PART 1 ###

def print_vecs(p, matrix):
    if p.vec[0] == 0:
        length = abs(p.vec[1])
        dim = "y"
        invert = p.vec[1] < 0
    else:
        length = abs(p.vec[0])
        dim = "x"
        invert = p.vec[0] < 0
    matrix[p.x1][p.y1] += 1
    x = p.x1
    y = p.y1
    for _ in range(length):
        if invert:
            if dim == "x":
                x -= 1
            else:
                y -= 1
        else:
            if dim == "x":
                x += 1
            else:
                y += 1
        matrix[x][y] += 1
    return matrix

def lines(data):
    data = [d.replace("\n", "") for d in data]
    # "0,9 -> 5,9" --> ((0,9), (5,9))
    data = [[
        int(d.split(" -> ")[0].split(",")[0]), int(d.split(" -> ")[0].split(",")[1]), 
        int(d.split(" -> ")[1].split(",")[0]), int(d.split(" -> ")[1].split(",")[1])
    ] for d in data]
    data = [d for d in data if d[0] == d[2] or d[1] == d[3]]
    df = pd.DataFrame(data)
    df.columns = ["x1", "y1", "x2", "y2"]
    max_x = max(max(df.x1), max(df.x2)) + 1
    max_y = max(max(df.y1), max(df.y2)) + 1
    matrix = np.zeros([max_x, max_y])
    df["vec"] = [(p.x2-p.x1, p.y2-p.y1) for _, p in df.iterrows()]
    for i, p in df.iterrows():  
        matrix = print_vecs(p, matrix)
    res = dict(Counter(itertools.chain(*matrix)))
    print(res)
    summe = 0
    summe = [summe+res[s] for s in res if s >= 2]
    return sum(summe)

### PART 2 ###


### EXECUTE ###

with open('data.txt') as f:
    data = f.readlines()

print(lines(data))
