import time

DEBUG = 0

if DEBUG:
	FILE = '../inputs/day04_debug.txt'
else:
	FILE = '../inputs/day04.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	numbers = []
	for line in data:
		all_numbers = line.split(': ')[1]
		seperated_numbers = all_numbers.split(' | ')
		winning_numbers = [int(x) for x in seperated_numbers[0].split()]
		card_numbers = [int(x) for x in seperated_numbers[1].split()]
		numbers.append({'winning_numbers': winning_numbers, 'card_numbers': card_numbers})
	return numbers


def part_one(data):
	total_points = 0
	for line in data:
		game_points = 0
		winning_numbers = 0
		for winning_number in line['winning_numbers']:
			if winning_number in line['card_numbers']:
				winning_numbers += 1
		if winning_numbers > 0:
			game_points = 2 ** (winning_numbers - 1)
		total_points += game_points
	return total_points



def part_two(data):
	card_count = {i: 1 for i in range(len(data))}
	for index, line in enumerate(data):
		winning_numbers = 0
		for winning_number in line['winning_numbers']:
			if winning_number in line['card_numbers']:
				winning_numbers += 1
		current_card_count = card_count[index]
		for i in range(index + 1, index + winning_numbers + 1):
			if i in card_count:
				card_count[i] += current_card_count


	return sum(card_count.values())


if __name__ == '__main__':
	data = load()
	data = parse(data)
	print(data)

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
