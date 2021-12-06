data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

### PART 1 ###

from src import lines

print(lines(data))

assert lines(data) == 5

### PART 2 ###

from src import lines_2

print(lines_2(data))

assert lines_2(data) == 12