import time

DEBUG = 0

if DEBUG:
	FILE = '../inputs/day01_debug.txt'
else:
	FILE = '../inputs/day01.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):		
	return data


def part_one(data):
	sum = 0
	for line in data:
		digits = []
		for char in line:
			if char >= '0' and char <= '9':
				digits.append((char))
		value = digits[0] + digits[-1]
		sum += int(value)
	return sum


def part_two(data):
	sum = 0
	for line in data:
		digits = []
		line = line.replace('one', 'o1e')
		line = line.replace('two', 't2o')
		line = line.replace('three', 't3e')
		line = line.replace('four', 'f4r')
		line = line.replace('five', 'f5e')
		line = line.replace('six', 's6x')
		line = line.replace('seven', 's7n')
		line = line.replace('eight', 'e8t')
		line = line.replace('nine', 'n9e')
		line = line.replace('zero', 'z0o')
		for char in line:
			if char >= '0' and char <= '9':
				digits.append((char))
		value = digits[0] + digits[-1]
		print(value)
		sum += int(value)
	return sum


if __name__ == '__main__':
	data = load()
	data = parse(data)
	print(data)

	# start_time = time.time()
	# print('Part One:', part_one(data))
	# print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
