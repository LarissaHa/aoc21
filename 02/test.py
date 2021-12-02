data = ["forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

### PART 1 ###

from src import navigate

print(navigate(data))

assert navigate(data) == (10, 15, 150)

### PART 2 ###

from src import aiming

print(aiming(data))

assert aiming(data) == (60, 15, 900)