import sys

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.read()
  return [int(c) for c in content.rstrip('\n').split('\t')]

def hash(cells):
  return ",".join(map(str, cells))

def distribute(cells):
  max_val = max(cells)
  index = cells.index(max_val)
  cells[index] = 0
  while (max_val > 0):
    index += 1
    if (index >= len(cells)):
      index = 0
    cells[index] += 1
    max_val -= 1

cells = readFile()
pattern = set([hash(cells)])
distribute(cells)
while hash(cells) not in pattern:
  pattern.add(hash(cells))
  distribute(cells)
print len(pattern)
