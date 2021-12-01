### PART 1 ###

def count_increases(data):
    count = 0
    for d in range(len(data)):
        if d == 0:
            pass
        else:
            if int(data[d]) > int(data[d-1]):
                count += 1
    return count

### PART 2 ###

def count_sliding_window_increases(data):
    count = 0
    for d in range(len(data)):
        try:
            A = int(data[d]) + int(data[d+1]) + int(data[d+2])
            B = int(data[d+1]) + int(data[d+2]) + int(data[d+3])
            if B > A:
                count += 1
        except IndexError:
            pass
    return count

### EXECUTE ###

with open('data.txt') as f:
    data = f.readlines()

print(count_increases(data))

print(count_sliding_window_increases(data))

