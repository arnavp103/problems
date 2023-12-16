from typing import List

input1 = """3,225,1,225,6,6,1100,1,238,225,104,0,2,171,209,224,1001,224,-1040,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,102,65,102,224,101,-3575,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,9,82,224,1001,224,-738,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1101,52,13,224,1001,224,-65,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1102,82,55,225,1001,213,67,224,1001,224,-126,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1,217,202,224,1001,224,-68,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1002,176,17,224,101,-595,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,20,92,225,1102,80,35,225,101,21,205,224,1001,224,-84,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1101,91,45,225,1102,63,5,225,1101,52,58,225,1102,59,63,225,1101,23,14,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,344,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,389,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,419,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,449,1001,223,1,223,1008,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,524,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,8,226,226,224,102,2,223,223,1005,224,554,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,569,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,584,1001,223,1,223,7,677,677,224,1002,223,2,223,1005,224,599,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,1107,226,226,224,102,2,223,223,1005,224,644,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,659,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226"""

def parse(input: str) -> List[int]:
	return [int(x) for x in input.split(',')]


def run(program: List[int]) -> List[int]:
	pc = 0
	while pc < len(program):
		operand = str(program[pc]).rjust(5, '0')
		_, mode2, mode1, instruction = int(operand[0]), int(operand[1]), int(operand[2]), int(operand[3:])
		if instruction == 99:
			break
		match instruction:
			case 1:
				if mode2 and mode1:
					program[program[pc + 3]] = program[pc + 1] + program[pc + 2]
				elif mode1:
					program[program[pc + 3]] = program[pc + 1] + program[program[pc + 2]]
				elif mode2:
					program[program[pc + 3]] = program[program[pc + 1]] + program[pc + 2]
				else:
					program[program[pc + 3]] = program[program[pc + 1]] + program[program[pc + 2]]
				pc += 4

			case 2:
				if mode2 and mode1:
					program[program[pc + 3]] = program[pc + 1] * program[pc + 2]
				elif mode1:
					program[program[pc + 3]] = program[pc + 1] * program[program[pc + 2]]
				elif mode2:
					program[program[pc + 3]] = program[program[pc + 1]] * program[pc + 2]
				else:
					program[program[pc + 3]] = program[program[pc + 1]] * program[program[pc + 2]]
				pc += 4

			case 3:
				program[program[pc + 1]] = int(input("Enter input: "))
				pc += 2

			case 4:
				if mode1:
					print(program[pc + 1])
				else:
					print(program[program[pc + 1]])
				pc += 2

	return program

def diagnostic() -> List[int]:
	program = parse(input1)
	return run(program)

# res = diagnostic()

# part 2
#			0, 1, 2,  3, 4, 5, 6, 7, 8, 9, 10,11,12, 13,  14,15,16, 17,18,19,20,21,22,23,24, 25,26,27,28,29,30,31,  32, 33,34,35,36,  37, 38,39,40,41,42,43,44,45,46
example2 = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"

def run2(program: List[int]) -> List[int]:
	pc = 0
	while pc < len(program):
		operand = str(program[pc]).rjust(5, '0')
		_, mode2, mode1, instruction = int(operand[0]), int(operand[1]), int(operand[2]), int(operand[3:])
		if instruction == 99:
			break
		noun, verb = program[pc + 1], program[pc + 2]
		try:
			if not mode1:
				noun = program[noun]
		except IndexError:
			pass
		try:
			if not mode2:
				verb = program[verb]
		except IndexError:
			pass


		# print(instruction, mode1, mode2, noun, verb, operand)

		match instruction:
			case 1:
				program[program[pc + 3]] = noun + verb
				pc += 4
			case 2:
				program[program[pc + 3]] = noun * verb
				pc += 4
			case 3:
				program[program[pc + 1]] = int(input("Enter input: "))
				pc += 2
			case 4:
				print(program[program[pc + 1]])
				pc += 2
			case 5:
				if noun:
					pc = verb
				else:
					pc += 3
			case 6:
				if not noun:
					pc = verb
				else:
					pc += 3
			case 7:
				if noun < verb:
					program[program[pc + 3]] = 1
				else:
					program[program[pc + 3]] = 0
				pc += 4
			case 8:
				if noun == verb:
					program[program[pc + 3]] = 1
				else:
					program[program[pc + 3]] = 0
				pc += 4
	return program

# run2(parse(example2))

def diagnostic2() -> List[int]:
	program = parse(input1)
	return run2(program)

res = diagnostic2()
