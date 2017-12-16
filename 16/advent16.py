import sys
from classes import parse, Spin, Partner, Exchange

def read_file():
  fileName = sys.argv[1]
  return [parse(move) for move in open(fileName).read().rstrip('\n').split(',')]

moves = read_file()
def dance(dancers, reps = 1):
  seen = []
  for i in range(reps):
    s = as_str(dancers)
    if s in seen:
      print(seen[reps % i])
      return
    seen.append(s)

    for move in moves:
      dancers = move.dance(dancers[:])
  print(as_str(dancers))

def as_str(dancers):
  return ''.join(dancers)

dancers = list("abcdefghijklmnop")
dance(dancers[:])
dance(dancers[:], 1000000000)