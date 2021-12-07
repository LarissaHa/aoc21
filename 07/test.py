data = [
"16,1,2,0,4,2,7,1,2,14"
]

### PART 1 ###

from src import fuel

print(fuel(data))

assert fuel(data) == (2, 37)

### PART 2 ###

from src import fuel_2

print(fuel_2(data))

assert fuel_2(data) == (5, 168)