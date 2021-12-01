data = ["199", 
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]

### PART 1 ###

from src import count_increases

assert count_increases(data) == 7

print(count_increases(data))

### PART 2 ###

from src import count_sliding_window_increases

assert count_sliding_window_increases(data) == 5

print(count_sliding_window_increases(data))