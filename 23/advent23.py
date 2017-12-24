import sys

def read_file():
  file = sys.argv[1]
  return [line.strip('\n').split(' ') for line in open(file).readlines()]

def valueof(val, registry):
  try:
    return int(val)
  except ValueError:
    return registry[val]

actions = read_file()
registry = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
i = 0
count = 0
seen = []
while i in range(len(actions)):
  (action, reg, val) = actions[i]
  if action == 'set':
    registry[reg] = valueof(val, registry)
  elif action == 'sub':
    registry[reg] -= valueof(val, registry)
  elif action == 'mul':
    registry[reg] *= valueof(val, registry)
    count += 1
  elif action == 'jnz':
    if valueof(reg, registry) != 0:
      i += valueof(val, registry)
      continue
  i += 1
  print(registry)


print(count)