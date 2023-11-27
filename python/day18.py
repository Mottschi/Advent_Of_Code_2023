import time

DEBUG = True

if DEBUG:
	FILE = '../inputs/day18_debug.txt'
else:
	FILE = '../inputs/day18.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	return data


def part_one(data):
	pass


def part_two(data):
	pass


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
