import time

DEBUG = 0

if DEBUG:
	FILE = '../inputs/day02_debug.txt'
else:
	FILE = '../inputs/day02.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	all_games = []
	for line in data:
		game_sets = []
		current_game = line.split(': ')[1].split('; ')
		for set in current_game:
			current_set = {'green': 0, 
					'red': 0, 
					'blue': 0}
			balls = set.split(', ')
			for current_balls in balls:
				num, color = current_balls.split()
				current_set[color] = int(num)
			game_sets.append(current_set)
		all_games.append(game_sets)
	return all_games


def part_one(data):
	max_amounts = {'green': 13, 
					'red': 12, 
					'blue': 14}
	valid_game_id_sums = 0
	for index, game in enumerate(data):
		valid = True
		print(game)
		for set in game:
			for color in set:
				if set[color] > max_amounts[color]:
					valid = False
					break
			if not valid:
				break
		if valid:
			valid_game_id_sums += index + 1
	return valid_game_id_sums


	


def part_two(data):
	summe = 0
	for game in data:
		max_amounts_required = {'green': 0, 
					'red': 0, 
					'blue': 0}
		for set in game:
			for color in set:
				if set[color] > max_amounts_required[color]:
					max_amounts_required[color] = set[color]
		power = max_amounts_required['blue'] * max_amounts_required['red'] * max_amounts_required['green']
		summe += power
	return summe


if __name__ == '__main__':
	data = load()
	data = parse(data)

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
