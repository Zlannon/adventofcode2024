def part1():
	l1 = []
	l2 = []
	with open("day1.txt") as f:
		for line in f:
			tmp = line.split(" ")
			l1.append(tmp[0])
			l2.append(tmp[3])
	l1.sort()
	l2.sort()

	dist = 0
	for i in range(len(l1)):
		dist += abs(int(l1[i]) - int(l2[i]))

	print(dist)
	f.close()

def part2():
	l1 = []
	l2 = []
	with open("day1.txt") as f:
		for line in f:
			tmp = line.split(" ")
			l1.append(tmp[0])
			l2.append(tmp[3])
	l1.sort()
	l2.sort()

	sim = 0
	for i in l1:
		for j in l2:
			if(int(i) == int(j)):
				sim += int(j)

	print(sim)
	f.close()

part1()
part2()