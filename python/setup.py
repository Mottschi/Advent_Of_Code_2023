'''
setup.py sets up the files for Advent of Code 2022 with some base code
to help reduce the time spend on setting up each individual day and instead
focus on actually solving the puzzle
'''

BLOCK_ACCIDENTAL_CHANGES = True

if BLOCK_ACCIDENTAL_CHANGES:
	import sys
	sys.exit('Setup currently locked. Change BLOCK_ACCIDENTAL_CHANGES to False if you want to create a fresh setup.\nWARNING: This will overwrite your existing files, if you have any.')


for i in range(1, 26):

	# Create empty text files for the input and debug input
	filename = f'../inputs/day{i:02}.txt'
	filename2 = f'../inputs/day{i:02}_debug.txt'
	open(filename, 'w').close()
	open(filename2, 'w').close()

	filename3 = f'day{i:02}.py'
	with open(filename3, 'w') as file:
		text = "import time\n\n"
		text += f"DEBUG = True\n\nif DEBUG:\n\tFILE = '{filename2}'\nelse:\n\tFILE = '{filename}'\n\n\n"
		text += "def load():\n\twith open(FILE) as file:\n\t\tarr = file.read().rstrip().split('\\n')\n\treturn arr\n\n\n"
		text += "def parse(data):\n\treturn data\n\n\n"
		text += "def part_one(data):\n\tpass\n\n\ndef part_two(data):\n\tpass\n\n\n"
		text += "if __name__ == '__main__':\n\t"
		text += "data = load()\n\tdata = parse(data)\n\tprint(data)\n\n\t"
		text += "start_time = time.time()\n\tprint('Part One:', part_one(data))\n\tprint(f'--- {time.time() - start_time} seconds ---')\n\t\n\t"
		text += "start_time = time.time()\n\tprint('Part Two:', part_two(data))\n\tprint(f'--- {time.time() - start_time} seconds ---')\n"

		file.write(text)