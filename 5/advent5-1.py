import sys

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.readlines()
  return [int(line.rstrip('\n')) for line in content]

def solve(instructions):
  steps = 0
  index = 0
  while 0 <= index and index < len(instructions):
    steps += 1
    jump = instructions[index]
    instructions[index] += 1
    index += jump
  print steps

instructions = readFile()
solve(instructions)
