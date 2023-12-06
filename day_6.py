from copy import deepcopy
import math

TIME = [44899691]
DISTANCE = [277113618901768]


def solve_part_1():
    all_ways = []
    for record_distance, time_allowed in zip(DISTANCE, TIME):
        num_ways = 0
        for time_moved in range(0, time_allowed):
            # speed = time you wait
            speed = deepcopy(time_moved)
            distance = (time_allowed - time_moved)* speed
                
            if distance > record_distance:
                num_ways += 1
        
        all_ways.append(num_ways)

    print(math.prod(all_ways))

solve_part_1()