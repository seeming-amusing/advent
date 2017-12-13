import sys

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.readlines()
  return [line.rstrip('\n') for line in content]

def count(line):
  skip_next = False
  is_garbage = False
  val = 1
  count = 0
  garbage_count = 0

  for c in stream:
    if skip_next:
      skip_next = False
      continue
    if c == '!':
      skip_next = True
      continue
    if is_garbage:
      if c == '>':
        is_garbage = False
      else:
        garbage_count += 1
    elif c == '{':
      if not is_garbage:
        count += val
        val += 1
    elif c == '}':
      if not is_garbage:
        val -= 1
    elif c == '<':
      is_garbage = True

  print count
  print garbage_count

streams = readFile()
for stream in streams:
  count(stream)
