import sys


def process(line):
	return [int(x.strip()) for x in line.rstrip('\n').split("\t")]

def readFile():
	fileName = sys.argv[1]
	with open(fileName) as f:
		content = f.readlines()
	content = [process(x) for x in content]
	return content

def difference(row):
	min = sys.maxint
	max = 0
	for val in row:
		if val > max:
			max = val
		if val < min:
			min = val
	return max - min

def checksum(spreadsheet):
	checksum = 0
	for row in spreadsheet:
		diff = difference(row)
		checksum += diff
	print checksum

#spreadsheet = [
#	[5, 17, 9, 5],
#	[17, 5, 3, 1],
#	[32, 4, 6, 8],
#	[1, 3, 95, 7]
#]

spreadsheet = readFile()
checksum(spreadsheet)
