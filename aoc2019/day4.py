def is_double(num: str) -> bool:
	for i in range(len(num) - 1):
		if num[i] == num[i + 1]:
			return True
	return False

def is_increasing(num: str) -> bool:
	for i in range(len(num) - 1):
		if num[i] > num[i + 1]:
			return False
	return True

def all_pws(start: int, end: int) -> int:
	count = 0
	for i in range(start, end + 1):
		if is_double(str(i)) and is_increasing(str(i)):
			count += 1
	return count


# 158126-624574
print(all_pws(158126, 624574))

# part 2

def is_purely_doubled(num: str) -> bool:
	for i in range(len(num) - 1):
		if num[i] == num[i + 1]:
			if i == 0:
				if num[i + 1] != num[i + 2]:
					return True
			elif i == len(num) - 2:
				if num[i] != num[i - 1]:
					return True
			elif num[i] != num[i - 1] and num[i + 1] != num[i + 2]:
				return True
	return False


def all_pws2(start: int, end: int) -> int:
	count = 0
	for i in range(start, end + 1):
		if is_purely_doubled(str(i)) and is_increasing(str(i)):
			count += 1
	return count

print(all_pws2(158126, 624574))
