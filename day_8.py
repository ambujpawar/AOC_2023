"""Day 8 Puzzle: Haunted Wasteland"""
import math
from utils.read_input import read_input


def process_data(task: str) -> list:
    """Read input data and return list of instructions"""
    input_data = read_input(task)
    instructions = input_data[0]
    maps = {}
    for line in input_data[2:]:
        start, connections = line.split('=')
        start = start.strip()
        left, right = connections.replace(')', '').replace('(', '').split(',')
        maps[start] = (left.strip(), right.strip())
    return instructions, maps


def solve_part_1(instructions, maps):
    start = 'AAA'
    end = 'ZZZ'

    curr_location = start
    special_i = 0
    i = 0

    while(True):
        if i > len(instructions) - 1:
            special_i = i % len(instructions)
        instruction = instructions[special_i]
        if instruction == 'L':
            index = 0
        else:
            index = 1
        curr_location = maps[curr_location][index]
        special_i += 1
        i += 1
        if curr_location == end:
            break

    print(f"Part 1: {i}")


def solve_part_2(instructions, maps):
    candidates_start = []
    candidates_end = []
    for k, v in maps.items():
        if k.endswith('A'):
            candidates_start.append(k)
        elif k.endswith('Z'):
            candidates_end.append(k)

    curr_locations = candidates_start.copy()

    steps_taken = [0] * len(curr_locations)
    for index, curr_location in enumerate(curr_locations):
        special_i = 0
        i = 0
        while(True):
            if i > len(instructions) - 1:
                special_i = i % len(instructions)
            instruction = instructions[special_i]
            if instruction == 'L':
                instruction_index = 0
            else:
                instruction_index = 1
            curr_location = maps[curr_location][instruction_index]
            curr_locations[index] = curr_location
            
            i += 1
            special_i += 1
            # If current_location ends with 'Z', then break
            if curr_location.endswith('Z'):
                steps_taken[index] = i
                break
    
    lcm = math.lcm(*steps_taken)
    print(f"Part 2: {lcm}")


if __name__ == "__main__":
    instructions, maps = process_data("data/day_8.txt")
    solve_part_1(instructions, maps)
    solve_part_2(instructions, maps)