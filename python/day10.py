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

REPLACEMENTS = {
	TOP_LEFT: ['.|.', '-J.', '...'],
	TOP_RIGHT: ['.|.', '.L-', '...'],
	TOP_BOTTOM: ['.|.', '.|.', '.|.'],
	LEFT_RIGHT: ['...','---', '...'],
	LEFT_BOTTOM: ['...', '-7.', '.|.'],
	RIGHT_BOTTOM: ['...', '.F-', '.|.'],
	GROUND: ['...', '...', '...'],
	'0': ['000', '000', '000'],
	'I': ['III', 'III', 'III']
}

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
		self.loop_tiles = {self.start}
		self.solved = False
		

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
		self.loop_tiles = set()
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
		self.loop_tiles.add(current_position)
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
			self.loop_tiles.add(current_position)
			step_count += 1
		self.solved = True
		return step_count // 2
	
	def upsize(self):
		upsized_map = []
		for line in self.map:
			new_line_top = ''
			new_line_center = ''
			new_line_bottom = ''
			for char in line:
				top, center, bottom = REPLACEMENTS[char]
				new_line_top += top
				new_line_center += center
				new_line_bottom += bottom
			upsized_map.append(new_line_top)
			upsized_map.append(new_line_center)
			upsized_map.append(new_line_bottom)
		self.map = [list(line) for line in upsized_map] 
		row, col = self.start
		row = row * 3 + 1
		col = col * 3 + 1
		self.start = row, col

		if self.solved:
			self.solve()


	def mark_non_pipe_tiles(self):
		if (not self.solved):
			self.solve()

		all_map_coords = set()

		for row in range(len(self.map)):
			for col in range(len(self.map[0])):
				all_map_coords.add((row, col))
		
		for row, col in all_map_coords - self.loop_tiles:
			self.map[row][col] =  'I' 

	def find_enclosed_tiles(self):
		tiles_changed = True
		row_count = len(self.map)
		col_count = len(self.map[0])
		marked_tiles = set()
		while tiles_changed:
			tiles_changed = False
			for row in range(0, row_count):
				for col in range(0, col_count):
					if (row, col) in self.loop_tiles or (row, col) in marked_tiles:
						continue
					if row == 0 or row == row_count-1 or col == 0 or col == col_count - 1:
						self.map[row][col] = '0'
						marked_tiles.add((row, col))
						tiles_changed = True
						continue
					neighbors = set()
					for row_mod in range(-1, 2):
						for col_mod in range(-1, 2):
							modified_row = row + row_mod
							modified_col = col + col_mod
							if modified_col < 0 or modified_col >= col_count or modified_row < 0 or modified_row >= row_count:
								continue
							neighbors.add(self.map[modified_row][modified_col])
					if '0' in neighbors:
						self.map[row][col] = '0'
						marked_tiles.add((row, col))
						tiles_changed = True
	
	def count_i_tiles(self):
		count = 0
		for row in self.map:
			for char in row:
				if char == 'I':
					count += 1
		return count
	
	def downsize(self):
		downsized_map = []
		row_count = len(self.map)
		col_count = len(self.map[0])
		for row in range(1, row_count, 3):
			line = []
			for col in range(1, col_count, 3):
				line.append(self.map[row][col])
			downsized_map.append(line)
		row, col = self.start
		self.start = ((row - 1) // 3, (col - 1) // 3)
		self.map = downsized_map
		print(self.start)
		print(self)

			

	def __str__(self) -> str:
		result = ''
		for line in self.map:
			result += ''.join(line) + '\n'
		# result += f'\nPipeTiles = {self.loop_tiles}'
		return result


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def part_one(data):
	my_map = Map(data)
	count = my_map.solve()
	return count
	

def part_two(data):
	my_map = Map(data)
	my_map.solve()
	my_map.upsize()
	my_map.mark_non_pipe_tiles()
	my_map.find_enclosed_tiles()
	print(my_map)
	my_map.downsize()
	return my_map.count_i_tiles()
	

	
	
	


if __name__ == '__main__':
	data = load()

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
