from tqdm import tqdm
from collections import Counter

### PART 1 ###

def grow(fish):
    new_fish = []
    for i in range(len(fish)):
        f = fish.pop(0)
        if f == 0:
            new_fish.append(6)
            new_fish.append(8)
        else:
            new_fish.append(f-1)
    return new_fish

def lanternfish(data, days):
    fish = [d.replace("\n", "") for d in data][0].split(",")
    fish = [int(f) for f in fish]
    for d in tqdm(range(days)):
        fish = grow(fish)
    return len(fish)

### PART 2 ###

def grow_2(f):
    return f-1

def lanternfish_2(data, days):
    fish = [d.replace("\n", "") for d in data][0].split(",")
    fish = [int(f) for f in fish]
    fish_dict = Counter(fish)
    for d in tqdm(range(days)):
        new_fish = {f-1: fish_dict[f] for f in fish_dict if f != 0}
        try:
            new_fish[8] = new_fish[8] + fish_dict[0]
        except KeyError:
            new_fish[8] = fish_dict[0]
        try:
            new_fish[6] = new_fish[6] + fish_dict[0]
        except KeyError:
            new_fish[6] = fish_dict[0]
        fish_dict = Counter(new_fish)

    return sum(fish_dict.values())

### EXECUTE ###

with open('data.txt') as f:
    data = f.readlines()

print(lanternfish_2(data, 256))
