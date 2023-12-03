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
