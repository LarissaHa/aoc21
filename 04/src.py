import pandas as pd
import numpy as np
from collections import Counter

### PART 1 ###

def preprocess(data):
    numbers = [int(n) for n in data[0].split(",")]
    fields = []
    f = []
    for line in data[1:]:
        if line == "":
            if len(f) > 1:
                fields.append(f)
            f = []
        points = [int(p) for p in line.split(" ") if p != ""]
        if points != []:
            f.append(points)
    fields.append(f)
    fields = [f for f in fields if f != []]
    return numbers, fields

def bingo(data):
    data = [d.replace("\n", "") for d in data]
    numbers, fields = preprocess(data)
    frames = [pd.DataFrame(f) for f in fields]
    for n in numbers:
        for f in range(len(frames)):
            frames[f] = frames[f].replace(n, np.nan)
            if 0.0 in set(frames[f].sum(axis=1)) or 0.0 in set(frames[f].sum()):
                summe = sum(frames[f].sum())
                last = n
                return summe, last, summe * last

### PART 2 ###

def bingo_last(data):
    """
    not finished - somehow produces wrong answer...?
    """
    data = [d.replace("\n", "") for d in data]
    numbers, fields = preprocess(data)
    frames = [pd.DataFrame(f) for f in fields]
    register = [i for i in range(len(frames))]
    for n in numbers:
        for f in range(len(frames)):
            if register[f] == np.nan:
                continue
            frames[f] = frames[f].replace(n, np.nan)
            if 0.0 in set(frames[f].sum(axis=1)) or 0.0 in set(frames[f].sum()):
                register[f] = np.nan
        if register.count(np.nan) == (len(frames)-1):
            for i in range(len(register)):
                if register[i] is not np.nan:
                    n = numbers[numbers.index(n)+1]
                    frames[i] = frames[i].replace(n, np.nan)
                    summe = sum(frames[i].sum())
                    last = n
                    return summe, last, summe * last

### EXECUTE ###

with open('data.txt') as f:
    data = f.readlines()

print(bingo(data))

print(bingo_last(data))