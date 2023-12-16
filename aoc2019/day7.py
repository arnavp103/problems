from typing import List, Tuple


input1 = """3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99"""

test1_ex1 = """3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"""

test1_ex2  = """3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"""


def parse1(input: str) -> List[int]:
	return [int(x) for x in input.split(",")]

def run(program: List[int], inputs: List[str]) -> Tuple[List[int], List[int]]:
	pc = 0
	input_idx = 0
	outs = []

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
				program[program[pc + 1]] = int(inputs[input_idx])
				input_idx += 1
				pc += 2
			case 4:
				outs.append(program[program[pc + 1]])
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

	return program, outs

def try_inputs(input: str) -> int:
	max = 0
	for a in range(5):
		for b in range(5):
			for c in range(5):
				for d in range(5):
					for e in range(5):
						if len(set([a, b, c, d, e])) == 5:
							settings = [str(a), str(b), str(c), str(d), str(e)]
							amps: List[int] = []
							for i in range(5):
								program = parse1(input)
								prev = 0
								if i > 0:
									prev = amps[i - 1]
								program, outs = run(program, [settings[i], str(prev)])
								amps.append(outs[-1])

							if amps[-1] > max:
								max = amps[-1]
	return max



res = try_inputs(input1)
print(res)

# part 2

test2_ex1 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"

def try_feedback_inputs(input: str) -> int:
	max = 0
	for a in range(5, 10):
		for b in range(5, 10):
			for c in range(5, 10):
				for d in range(5, 10):
					for e in range(5, 10):
						if len(set([a, b, c, d, e])) == 5:
							settings = [str(a), str(b), str(c), str(d), str(e)]
							amps: List[int] = []
							for i in range(5):
								program = parse1(input)
								prev = 0
								if i > 0:
									prev = amps[i - 1]
								program, outs = run(program, [settings[i], str(prev)])
								amps.append(outs[-1])

							# feedback
							program = parse1(input)
							prev = 0
							while True:
								for i in range(5):
									program, outs = run(program, [settings[i], str(prev)])
									prev = outs[-1]
									if i == 4 and program[0] == 99:
										if prev > max:
											max = prev
										break
	return max

res = try_feedback_inputs(test2_ex1)
print(res)