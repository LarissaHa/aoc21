### PART 1 ###

def navigate(data):
    data = [(d.split(" ")[0], int(d.split(" ")[1])) for d in data]
    depth, horiz = 0, 0
    for d in data:
        if d[0] == "forward":
            horiz = horiz + d[1]
        elif d[0] == "down":
            depth = depth + d[1]
        elif d[0] == "up":
            depth = depth - d[1]
        else:
            print(d)
            print("this should not be possible, doing nothing")
    return depth, horiz, depth * horiz

### PART 2 ###

def aiming(data):
    data = [(d.split(" ")[0], int(d.split(" ")[1])) for d in data]
    depth, horiz, aim = 0, 0, 0
    for d in data:
        if d[0] == "forward":
            horiz = horiz + d[1]
            depth = depth + (aim * d[1])
        elif d[0] == "down":
            aim = aim + d[1]
        elif d[0] == "up":
            aim = aim - d[1]
        else:
            print(d)
            print("this should not be possible, doing nothing")
    return depth, horiz, depth * horiz

### EXECUTE ###

with open('data.txt') as f:
    data = f.readlines()

print(navigate(data))

print(aiming(data))