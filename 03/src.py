import pandas as pd

### PART 1 ###

def consumption(data):
    data = [d.replace("\n", "") for d in data]
    data = [list(d) for d in data]
    gamma, epsilon = "", ""
    df = pd.DataFrame(data)
    for c in df.columns:
        gamma = gamma + df[c].value_counts().index[0]
        try:
            epsilon = epsilon + df[c].value_counts().index[1]
        except IndexError:
            if df[c].value_counts().index[0] == "0":
                epsilon = epsilon + "1"
            else:
                epsilon = epsilon + "0"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma, epsilon, gamma * epsilon

### PART 2 ###

def get_last_number(v, df):
    mapping = {0: "1", 1: "0"}
    for c in df.columns:
        target = df[c].value_counts().index[v]
        if df[c].value_counts()[0] == df[c].value_counts()[1]:
            target = mapping[v]
        df = df[df[c] == target]
        if len(df) == 1:
            return "".join(df.values[0])

def lifesupport(data):
    data = [d.replace("\n", "") for d in data]
    data = [list(d) for d in data]
    df = pd.DataFrame(data)
    oxygen = int(get_last_number(0, df), 2)
    co2 = int(get_last_number(1, df), 2)
    return oxygen, co2, oxygen * co2

### EXECUTE ###

with open('data.txt') as f:
    data = f.readlines()

print(consumption(data))

print(lifesupport(data))