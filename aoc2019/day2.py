from typing import List


input = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"""

test = "1,9,10,3,2,3,11,0,99,30,40,50"

def parse(input: str) -> List[int]:
	return [int(x) for x in input.split(',')]


def run(program: List[int]) -> List[int]:
	pc = 0
	for instruction in program[::4]:
		if instruction == 99:
			break
		elif instruction == 1:
			program[program[pc + 3]] = program[program[pc + 1]] + program[program[pc + 2]]
		elif instruction == 2:
			program[program[pc + 3]] = program[program[pc + 1]] * program[program[pc + 2]]
		pc += 4
	return program

def twelve_o_two() -> List[int]:
	program = parse(input)
	program[1] = 12
	program[2] = 2
	return run(program)

res = twelve_o_two()
print(res[0])

# part 2

def find_noun_verb() -> int:
	for noun in range(100):
		for verb in range(100):
			program = parse(input)
			program[1] = noun
			program[2] = verb
			if run(program)[0] == 19690720:
				return 100 * noun + verb
	return -1


print(find_noun_verb())