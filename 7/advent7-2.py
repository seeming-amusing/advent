import sys

class Program:

  def __init__(self, name, weight, discs):
    self.name = name
    self.weight = weight
    self.discs = discs
    self.adjusted_weight = weight
    self.parent = ""

  def __str__(self):
    return "Program '" + self.name + "' { adjusted_weight: " + str(self.adjusted_weight) + ", children: " + str(self.discs) + "}"

  def __repr__(self):
    return "Program '" + self.name + "' { adjusted_weight: " + str(self.adjusted_weight) + ", children: " + str(self.discs) + "}"

  def adjust(self, tower):
    if len(self.discs) > 0:
      weight = self.weight
      for disc in self.discs:
        weight += tower[disc].adjust(tower)
      self.adjusted_weight = weight
    return self.adjusted_weight

  def set_parent(self, parent):
    self.parent = parent

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.readlines()
  return dict(parse(line.rstrip('\n')) for line in content)

def parse(line):
  line = line.split(" -> ")
  discs = list()
  if (len(line) > 1):
    discs = line[1].split(", ")
  line = line[0].split(" ")
  return (line[0], Program(line[0], int(line[1].translate(None, "()")), discs))

def find_root(tower):
  keys = list(tower.keys())
  for disc in tower.values():
    disc.adjust(tower)
    for child in disc.discs:
      keys.remove(child)
      tower[child].set_parent(disc.name)
  return keys[0]

def children_mismatch(program, tower):
  weights = map(lambda v: v.adjusted_weight, [tower[k] for k in program.discs])
  print weights
  if weights.count(min(weights)) == 1:
    return weights.index(min(weights))
  elif weights.count(max(weights)) == 1:
    return weights.index(max(weights))
  return -1

tower = readFile()
root = find_root(tower)
current = tower[root]
index = children_mismatch(current, tower)
while index != -1:
  current = tower[current.discs[index]]
  index = children_mismatch(current, tower)
print current.weight
