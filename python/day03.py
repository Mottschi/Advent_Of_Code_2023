import time

DEBUG = False

if DEBUG:
	FILE = '../inputs/day03_debug.txt'
else:
	FILE = '../inputs/day03.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	return data


def part_one(data):
	ROW_LENGTH = len(data[0])
	COL_LENGTH = len(data)
	DIGITS = '0123456789'
	BLANKS = '.'

	summe = 0

	for y in range(COL_LENGTH):
		current_number = ''
		include_current_number = False
		for x in range(ROW_LENGTH):
			current_char = data[y][x]
			if current_char in DIGITS:
				# while parsing a number, we go through these steps:

				# 1: add the digit to the current number
				current_number += current_char

				# 2: if we are not sure yet whether current number should be included
				#    we need to check neighbors for symbols
				if not include_current_number:
					for mod_y in range(-1, 2):
						if include_current_number:
							break
						for mod_x in range(-1, 2):
							if include_current_number:
								break

							neighbor_loc_x = x + mod_x
							neighbor_loc_y = y + mod_y
							if neighbor_loc_x < 0 or neighbor_loc_x >= ROW_LENGTH or neighbor_loc_y < 0 or neighbor_loc_y >= COL_LENGTH:
								continue
							neighbor_char = data[neighbor_loc_y][neighbor_loc_x] 
							if neighbor_char not in DIGITS and neighbor_char not in BLANKS:
								include_current_number = True


				# 3: check if we are at the final digit
				#    (either because the line is at the end, or the next symbol is not a digit)
				if (x == ROW_LENGTH - 1) or (data[y][x+1] not in DIGITS):
					# we are at the final digit, so we check whether the number should be included 
					# if so, add it to the result sum
					if include_current_number:
						summe += int(current_number)
					# in any way, when at the end, we need to reset current number and inclusion check
					current_number = ''
					include_current_number = False
	return summe	

				



def part_two(data):
	ROW_LENGTH = len(data[0])
	COL_LENGTH = len(data)
	DIGITS = '0123456789'
	GEAR_SYMBOL = '*'

	result = 0

	# rather then checking all numbers for gear symbol neighbors, we look for the gear symbols directly
	# and then check how many numbers they have as neighbors

	for y in range(COL_LENGTH):
		if GEAR_SYMBOL not in data[y]:
			continue
		for x in range(ROW_LENGTH):
			current_char = data[y][x]
			if current_char == GEAR_SYMBOL:
				found_neighbors_count = 0
				found_neighbors_coords = []
				# when we find a gear symbol, we need to check the neighbors to find numbers
				# the two neighbors in the current line we can check directly for digits, each digit
				# found there indicates a number
				if x > 0 and data[y][x-1] in DIGITS:
					found_neighbors_count += 1
					found_neighbors_coords.append((y, x-1))

				if x < ROW_LENGTH - 1 and data[y][x+1] in DIGITS:
					found_neighbors_count += 1
					found_neighbors_coords.append((y, x+1))

				# for the lines above and below the current line, it is a bit more tricky
				# if the middle character of the three neighbors in that line is a digit, then there is exactly one neighbor in that line
				# otherwise, we need to check both corner characters, each digit found there adds one neighbor number
				if y > 0:
					if data[y-1][x] in DIGITS:
						found_neighbors_count += 1
						found_neighbors_coords.append((y-1, x))
					else:
						if x > 0 and data[y-1][x-1] in DIGITS:
							found_neighbors_count += 1
							found_neighbors_coords.append((y-1, x-1))

						if x < ROW_LENGTH - 1 and data[y-1][x+1] in DIGITS:
							found_neighbors_count += 1
							found_neighbors_coords.append((y-1, x+1))
				
				if y < COL_LENGTH - 1:
					if data[y+1][x] in DIGITS:
						found_neighbors_count += 1
						found_neighbors_coords.append((y+1, x))
					else:
						if x > 0 and data[y+1][x-1] in DIGITS:
							found_neighbors_count += 1
							found_neighbors_coords.append((y+1, x-1))

						if x < ROW_LENGTH - 1 and data[y+1][x+1] in DIGITS:
							found_neighbors_count += 1
							found_neighbors_coords.append((y+1, x+1))

				if found_neighbors_count == 2:
					# parse both numbers, cast to int and multiply, then add result to result
					numbers = []
					for n_y, n_x in found_neighbors_coords:
						while n_x > 0 and data[n_y][n_x-1] in DIGITS:
							n_x -= 1
						number = ''
						while n_x < ROW_LENGTH and data[n_y][n_x] in DIGITS:
							number += data[n_y][n_x]
							n_x += 1
						numbers.append(int(number))
					result += numbers[0] * numbers[1]

	return result	


if __name__ == '__main__':
	data = load()
	data = parse(data)

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
