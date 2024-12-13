def checkSafe(tmp):
	totalSafe = 0
	increasing = 0
	if(int(tmp[0]) - int(tmp[1]) < 0):
		increasing = 1
	inc = 1
	for i in range(len(tmp) - 1):
		tmp[i] = int(tmp[i])
		tmp[i + 1] = int(tmp[i + 1])
		if increasing:
			if tmp[i] - tmp[i+1] >= 0:
				inc = 0
				break
			if tmp[i] - tmp[i+1] < -3:
				inc = 0
				break
		else:
			if tmp[i] - tmp[i+1] <= 0:
				inc = 0
				break
			if tmp[i] - tmp[i+1] > 3:
				inc = 0
				break
	if(inc):
		totalSafe = 1
	return totalSafe

def part1():
	totalSafe = 0
	with open("day2.txt") as f:
		for line in f:
			increasing = 0
			tmp = line.split(" ")
			totalSafe += checkSafe(tmp)
	print("part1:", totalSafe)

def part2():
	totalSafe = 0
	with open("day2.txt") as f:
		for line in f:
			tmp = line.split(" ")
			for j in range(len(tmp)):
				tmp2 = tmp.pop(j)
				if(checkSafe(tmp)):
					totalSafe += 1
					break
				tmp.insert(j, tmp2)
	print("part2:", totalSafe)

part1()
part2()