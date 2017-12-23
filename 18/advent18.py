import sys

def read_file():
  file = sys.argv[1]
  return [line.strip('\n').split(' ') for line in open(file).readlines()]

def valueof(val, registry):
  try:
    return int(val)
  except ValueError:
    return registry[val]

duet = read_file()
registry = dict()
i = 0
last_sound = None
while i in range(len(duet)):
  action, reg = duet[i][0], duet[i][1]
  if reg not in registry:
    registry[reg] = 0
  if action == 'snd':
    last_sound = registry[reg]
  elif action == 'set':
    registry[reg] = valueof(duet[i][2], registry)
  elif action == 'add':
    registry[reg] += valueof(duet[i][2], registry)
  elif action == 'mul':
    registry[reg] *= valueof(duet[i][2], registry)
  elif action == 'mod':
    registry[reg] %= valueof(duet[i][2], registry)
  elif action == 'rcv':
    if registry[reg] != 0:
      break
  elif action == 'jgz':
    if registry[reg] > 0:
      i += valueof(duet[i][2], registry)
      continue
  i += 1
print(last_sound)