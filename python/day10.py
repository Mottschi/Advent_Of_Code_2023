import time

DEBUG = 0

if DEBUG:
	FILE = '../inputs/day10_debug.txt'
else:
	FILE = '../inputs/day10.txt'


START = 'S'
TOP_LEFT = 'J'
TOP_RIGHT = 'L'
TOP_BOTTOM = '|'
LEFT_RIGHT = '-'
LEFT_BOTTOM = '7'
RIGHT_BOTTOM = 'F'
GROUND = '.'

class Map:
	def __init__(self, data):
		lines = [list(line) for line in data]
		row_count = len(lines)
		col_count = len(lines[0])
		start = None
		for i in range(len(data)):
			line = data[i]
			if start is None:
				start_index = line.find(START)
				if start_index != -1:
					start = (i, start_index)
					break
		self.start = start
		self.map = lines

		row, col = self.start
		connections = []

		if row > 0 and self.map[row - 1][col] in [TOP_BOTTOM, LEFT_BOTTOM, RIGHT_BOTTOM]:
			connections.append('TOP')
		if col > 0 and self.map[row][col - 1] in [TOP_RIGHT, LEFT_RIGHT, RIGHT_BOTTOM]:
			connections.append('LEFT')
		if col < col_count - 1 and self.map[row][col + 1] in [LEFT_BOTTOM, LEFT_RIGHT, TOP_LEFT]:
			connections.append('RIGHT')
		if row < row_count - 1 and self.map[row+1][col] in [TOP_BOTTOM, TOP_LEFT, TOP_RIGHT]:
			connections.append('BOTTOM')
		
		assert len(connections) == 2

		connection = connections[0] + '_' + connections[1]
		connection_value = eval(connection)
		
		self.map[row][col] = connection_value

	def solve(self) -> int:
		last_position = self.start
		row, col = last_position
		current_pipe = self.map[row][col]
		next_position = None
		if current_pipe in [TOP_BOTTOM, TOP_LEFT, TOP_RIGHT]:
			next_position = (row-1, col)
		elif current_pipe in [LEFT_BOTTOM, RIGHT_BOTTOM]:
			next_position = (row+1, col)
		else:
			# if it does not go top or bottom, pipe must go left right
			next_position = (row, col+1)
		current_position = next_position
		step_count = 1
		while current_position != self.start:
			row, col = current_position
			current_pipe = self.map[row][col]
			options = set()
			top = row - 1, col
			bottom = row + 1, col
			left = row, col - 1
			right = row, col + 1
			if current_pipe == TOP_BOTTOM:
				options.add(top)
				options.add(bottom)
			elif current_pipe == TOP_LEFT:
				options.add(top)
				options.add(left)
			elif current_pipe == TOP_RIGHT:
				options.add(top)
				options.add(right)
			elif current_pipe == LEFT_BOTTOM:
				options.add(left)
				options.add(bottom)
			elif current_pipe == LEFT_RIGHT:
				options.add(left)
				options.add(right)
			elif current_pipe == RIGHT_BOTTOM:
				options.add(right)
				options.add(bottom)
			else:
				raise ValueError('Unknown pipe')
			
			for tile in options:
				if tile == last_position:
					continue
				next_position = tile
			
			last_position = current_position
			current_position = next_position
			step_count += 1

		return step_count // 2


	def __str__(self) -> str:
		result = ''
		for line in self.map:
			result += ''.join(line) + '\n'
		return result


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def part_one(data):
	my_map = Map(data)
	return my_map.solve()
	

def part_two(data):
	pass


if __name__ == '__main__':
	data = load()

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
