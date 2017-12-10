import sys
from collections import namedtuple

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.readlines()
  return [parse(line.rstrip('\n')) for line in content]

def parse(line):
  line = line.split(" -> ")
  discs = list()
  if (len(line) > 1):
    discs = line[1].split(", ")
  line = line[0].split(" ")
  return Program(line[0], int(line[1].translate(None, "()")), discs)

Program = namedtuple("Program", ["name", "weight", "discs"])
tower = readFile()
base_discs = [d for d in tower if len(d.discs) != 0]
keys = map(lambda p: p.name, tower)
for disc in base_discs:
  for child in disc.discs:
    keys.remove(child)
print keys