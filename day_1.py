"""
Welcome to the first day of Advent of Code 2022!
"""
import re
from typing import Any, List
from utils.read_input import read_input

MAPPING = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six' : 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def solve_part_1(input_data: List[Any]):
    """
    - Iterate through the data
    - Extract digits from a line
    - Find the first and last digit in each line
    - Join the digits to form a 2-digit number
    """
    code = []
    
    for line in input_data:
        # Extract digits from a line
        digits = [int(digit) for digit in line if digit.isdigit()]

        # Find the first and last digit in each line
        first_digit = digits[0]
        last_digit = digits[-1]

        # Join the digits to form a 2-digit number
        number = first_digit * 10 + last_digit
        code.append(number)
    
    answer = sum(code)
    return answer


def solve_part_2(input_data: List[Any]):
    """
    - Iterate through the data
    - Extract digits on each line they can also be strings like: one, two, three
    - Find the first and last digit in each line
    - Join the digits to form a 2-digit number

    Sample input:
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    Return: 29, 83, 13, 24, 42, 14, 76
    """
    acceptable_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    code = []

    for line in input_data:
        # Extract digits on each line and include index as well
        digits = [(index, digit) for index, digit in enumerate(line) if digit.isdigit()]

        # Find if the line contains any of the acceptable numbers and find index
        for num in acceptable_nums:
            indexes = [m.start() for m in re.finditer(num, line)]
            if indexes:
                for index in indexes:
                    digits.append((index, num))


        # Find the entries with the smallest and largest index
        first_digit = min(digits)[1]
        last_digit = max(digits)[1]
        
        if first_digit.isdigit():
            first_digit = int(first_digit)
        else:
            first_digit = MAPPING[first_digit]
        
        if last_digit.isdigit():
            last_digit = int(last_digit)
        else:
            last_digit = MAPPING[last_digit]
        
        number = first_digit * 10 + last_digit
        code.append(number)

    print(code[:10])
    answer = sum(code)
    return answer


def main():
    """
    Main entry point of the script.
    """
    input_data = read_input('data/day_1.txt')
    answer = solve_part_1(input_data)
    print(f'Part 1: {answer}')

    answer_2 = solve_part_2(input_data)
    print(f'Part 2: {answer_2}')


if __name__ == '__main__':
    main()