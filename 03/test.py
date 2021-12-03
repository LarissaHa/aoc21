data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

### PART 1 ###

from src import consumption

print(consumption(data))

assert consumption(data) == (22, 9, 198)

### PART 2 ###

from src import lifesupport

print(lifesupport(data))

assert lifesupport(data) == (23, 10, 230)