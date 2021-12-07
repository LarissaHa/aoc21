from tqdm import tqdm
from collections import Counter

### PART 1 ###

def calc_cost(submarines, sub):
    target = submarines[sub]
    difference = [abs(pos-sub) for pos in submarines]
    return sum(difference)

def fuel(data):
    submarines = [d.replace("\n", "") for d in data][0].split(",")
    submarines = [int(sub) for sub in submarines]
    fuel_cost = {}
    for sub in tqdm(range(len(submarines))):
        fuel_cost[sub] = calc_cost(submarines, sub)
    return [key for key in fuel_cost if fuel_cost[key] == min(fuel_cost.values())][0], min(fuel_cost.values())

### PART 2 ###

def more_costs(d):
    n = 0
    for i in range(d):
        n = n+(i+1)
    return n

def calc_cost_2(submarines, sub):
    target = submarines[sub]
    difference = [more_costs(abs(pos-sub)) for pos in submarines]
    return sum(difference)

def fuel_2(data):
    submarines = [d.replace("\n", "") for d in data][0].split(",")
    submarines = [int(sub) for sub in submarines]
    fuel_cost = {}
    for sub in tqdm(range(len(submarines))):
        fuel_cost[sub] = calc_cost_2(submarines, sub)
    return [key for key in fuel_cost if fuel_cost[key] == min(fuel_cost.values())][0], min(fuel_cost.values())

### EXECUTE ###

with open('data.txt') as f:
    data = f.readlines()

print(fuel(data))

print(fuel_2(data))
