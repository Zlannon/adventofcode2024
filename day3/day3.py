import re

def mul(x,y):
	return x*y

def part1():
	allMuls = []
	pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
	with open("day3.txt") as f:
		for line in f:
			allMuls += re.findall(pattern, line)

	soln = 0
	for i in allMuls:
		soln += eval(i)
	print("part 1:", soln)

def part2():
	allMuls = []
	pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)"
	with open("day3.txt") as f:
		for line in f:
			allMuls += re.findall(pattern, line)

	mulEnabled = 1
	soln = 0
	for i in allMuls:
		if(i == "don't()"):
			mulEnabled = 0
			continue
		if(i == "do()"):
			mulEnabled = 1
			continue
		if(mulEnabled):
			soln += eval(i)
	print("part 2:", soln)

part1()
part2()