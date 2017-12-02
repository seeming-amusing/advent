from __future__ import division
import sys

def process(line):
	return [int(x.strip()) for x in line.rstrip('\n').split("\t")]

def readFile():
	fileName = sys.argv[1]
	with open(fileName) as f:
		content = f.readlines()
	content = [process(x) for x in content]
	return content

def calculate(x, y):
	if x > y:
		result = x / y
	else:
		result = y / x
	if result.is_integer():
		return result

def divisor(row):
	result = 0
	for i, x in enumerate(row):
		for y in row[i + 1 : len(row)]:
			temp = calculate(x, y)
			if temp is not None and temp > result:
				result = int(temp)
	return result

def checksum(spreadsheet):
	checksum = 0
	for row in spreadsheet:
		diff = divisor(row)
		checksum += diff
	print checksum

spreadsheet = readFile()
checksum(spreadsheet)
