import math
import re
from utils.read_input import read_input

MAX_BALLS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_string(input_string):
    # Regular expression pattern to match the game number
    game_number_pattern = re.compile(r'Game (\d+):')

    # Regular expression pattern to match color quantities
    color_pattern = re.compile(r'(\d+) (\w+)')

    # Find all matches for game number
    game_numbers = int(game_number_pattern.findall(input_string)[0])

    if game_numbers:
        # Initialize a list to store game data
        game_data_list = []

        # Process each game number
        # Find num_instances of semi-colon in string
        num_games = input_string.count(';') + 1

        start_index = input_string.find(":") + 1

        for game_number in range(num_games):
            # Find the start and end indices of the current game
            end_index = input_string.find(';', start_index) if ';' in input_string[start_index:] else len(input_string)

            # Extract the substring for the current game
            game_data_str = input_string[start_index:end_index]

            # Process color quantities using the color pattern
            game_data = {}
            quantities = color_pattern.findall(game_data_str)
            for qty, color in quantities:
                game_data[color] = int(qty)

            game_data_list.append((int(game_number), game_data))
            start_index = end_index + 1

        return (game_numbers, game_data_list)

    else:
        print("Invalid input string format")


def solve_part_1(input_data):
    """
    """
    # Parse the input string
    impossible_games = set()
    all_games = set(range(1,101))

    for input_string in input_data:
        game_number, game_data_list = parse_string(input_string)

        # Iterate over each game
        for game_data in game_data_list:            
            # Iterate over each color   
            for color, qty in game_data[1].items():
                if qty > MAX_BALLS[color]:
                    impossible_games.add(game_number)
                    break

    possible_games = all_games - impossible_games
    return sum(possible_games)


def solve_part_2(input_data):
    """
    Finding minimum number of balls required for each color
    is equivalent to finding the maximum number of balls per color
    """
    code_values = []
    for input_string in input_data:
        game_number, game_data_list = parse_string(input_string)
        max_balls_per_color = {"red": 0, 'green': 0, 'blue': 0}
        for game_data in game_data_list:
            for color, qty in game_data[1].items():
                if qty > max_balls_per_color[color]:
                    max_balls_per_color[color] = qty
        code_values.append(math.prod(max_balls_per_color.values()))
    
    return sum(code_values)


def main():
    """
    Main entry point of the script.
    """
    input_data = read_input('data/day_2.txt')
    answer = solve_part_1(input_data)
    print(f'Part 1: {answer}')

    answer_2 = solve_part_2(input_data)
    print(f'Part 2: {answer_2}')


if __name__ == '__main__':
    main()



