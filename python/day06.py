import time

DEBUG = 0

if DEBUG:
	FILE = '../inputs/day06_debug.txt'
else:
	FILE = '../inputs/day06.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	time = data[0].split()[1:]
	distance = data[1].split()[1:]
	return time, distance

def prod(arr):
	result = 1
	for e in arr:
		result *= e
	return result

def conc(arr):
	result = ''
	for e in arr:
		result += e
	return result

def part_one(data):
	time = [int(e) for e in data[0]]
	distance = [int(e) for e in data[1]]
	results = []
	for race in range(len(time)):
		count = 0
		race_time = time[race]
		race_distance = distance[race]
		for hold_time in range(1, race_time):
			if (race_time - hold_time) * hold_time > race_distance:
				count += 1
		results.append(count)
	result = prod(results)
	return result


def part_two(data):
	race_time = int(conc(data[0]))
	race_distance = int(conc(data[1]))
	print(race_time, race_distance)
	peak_time = race_time // 2
	first_winning_hold_time = None
	first_winning_distance = None
	for hold_time in range(1, peak_time + 1):
		distance = (race_time - hold_time) * hold_time
		if distance > race_distance:
			first_winning_hold_time = hold_time
			first_winning_distance = distance
			break
	if first_winning_hold_time is None:
		raise Error('No winning times found')
	print(first_winning_hold_time, first_winning_distance, first_winning_distance + first_winning_hold_time)
	count = race_time - 2 * first_winning_hold_time + 1
	return count



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
