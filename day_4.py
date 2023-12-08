from utils.read_input import read_input


def solve_part_1(input_data):
    answer = 0

    for line in input_data:
        start = line.find(':')
        cards = line[start+1:]
        winning_nums, my_nums = cards.split('|')
        
        # Set comprehension
        winning_nums = {int(num) for num in winning_nums.split()}
        my_nums = {int(num) for num in my_nums.split()}
        num_common = len(winning_nums.intersection(my_nums))
        if num_common:
            answer += 2**(num_common-1)

    return answer


def solve_part_2(input_data):
    all_cards = [1] * len(input_data)
    for card_num, line in enumerate(input_data):
        start = line.find(':')
        cards = line[start+1:]
        winning_nums, my_nums = cards.split('|')
        # Set comprehension
        winning_nums = {int(num) for num in winning_nums.split()}
        my_nums = {int(num) for num in my_nums.split()}
        num_common = len(winning_nums.intersection(my_nums))
    
        for c in range(card_num, card_num+num_common):
            all_cards[c+1] += all_cards[card_num]

    answer = sum(all_cards)
    return answer


def Main():
    input_data = read_input("data/day_4.txt")
    answer = solve_part_1(input_data)
    print(f"Part 1: {answer}")

    answer = solve_part_2(input_data)
    print(f"Part 2: {answer}")


if __name__ == '__main__':
    Main()
