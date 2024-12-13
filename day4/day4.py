def checkMas(wordsearch, i, j):
	words = []
	numXmas = 0
	if(j - 3 >= 0):
		words.append(wordsearch[i][j-3:j+1][::-1])
		if(i - 3 >= 0):
			words.append((wordsearch[i-3][j-3] + wordsearch[i-2][j-2] + wordsearch[i-1][j-1] + wordsearch[i][j])[::-1])
		if(i + 3 < len(wordsearch)):
			words.append((wordsearch[i+3][j-3] + wordsearch[i+2][j-2] + wordsearch[i+1][j-1] + wordsearch[i][j])[::-1])
	if(j + 3 < len(wordsearch[i])):
		words.append(wordsearch[i][j:j+4])
		if(i - 3 >= 0):
			words.append(wordsearch[i][j] + wordsearch[i-1][j+1] + wordsearch[i-2][j+2] + wordsearch[i-3][j+3])
		if(i + 3 < len(wordsearch)):
			words.append(wordsearch[i][j] + wordsearch[i+1][j+1] + wordsearch[i+2][j+2] + wordsearch[i+3][j+3])
	if(i - 3 >= 0):
		words.append((wordsearch[i-3][j] + wordsearch[i-2][j] + wordsearch[i-1][j] + wordsearch[i][j])[::-1])
	if(i + 3 < len(wordsearch)):
		words.append(wordsearch[i][j] + wordsearch[i+1][j] + wordsearch[i+2][j] + wordsearch[i+3][j])
	for word in words:
		if word == "XMAS":
			numXmas += 1
	return numXmas

def checkXMAS(wordsearch, i, j):
	words = []
	numXmas = 0
	if(j - 1 < 0 or j + 1 >= len(wordsearch[i]) or i-1 < 0 or i + 1 >= len(wordsearch)):
		return 0
	words.append(wordsearch[i-1][j-1] + wordsearch[i][j] + wordsearch[i+1][j+1])
	words.append(wordsearch[i-1][j+1] + wordsearch[i][j] + wordsearch[i+1][j-1])
	words.append((wordsearch[i-1][j-1] + wordsearch[i][j] + wordsearch[i+1][j+1])[::-1])
	words.append((wordsearch[i-1][j+1] + wordsearch[i][j] + wordsearch[i+1][j-1])[::-1])
	for word in words:
		if word == "MAS":
			numXmas += 1
	if numXmas == 2:
		return 1
	return 0


def part1():
	wordsearch = []
	with open("day4.txt") as f:
		for line in f:
			wordsearch.append(line.replace("\n",""))
	numWords = 0
	for i in range(len(wordsearch)):
		for j in range(len(wordsearch[i])):
			if(wordsearch[i][j] == 'X'):
				numWords += checkMas(wordsearch, i, j)
	print("part1:", numWords)

def part2():
	wordsearch = []
	with open("day4.txt") as f:
		for line in f:
			wordsearch.append(line.replace("\n",""))
	numWords = 0
	for i in range(len(wordsearch)):
		for j in range(len(wordsearch[i])):
			if(wordsearch[i][j] == 'A'):
				numWords += checkXMAS(wordsearch, i, j)
	print("part2:", numWords)

part1()
part2()