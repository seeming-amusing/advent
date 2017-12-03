import math
import sys

def stats(val):
  if val <= 1:
    return (0, 0, 0)

  root = int(math.ceil(math.sqrt(val)))
  if math.pow(root, 2) == val:
    return (val, root - 1, (root - 1) / 2)

  root += 1 if (root % 2 == 0) else 0
  max = root if root % 2 == 0 else root - 1
  min = max / 2
  return (int(math.pow(root, 2)), max, min)

def calculate(stats):
  current = stats[0]
  while current - stats[1] >= entry:
    current -= stats[1]
  diff = current - entry
  if diff > stats[2]:
    print stats[2] + (diff - stats[2])
  else:
    print stats[1] - diff

entry = int(sys.argv[1])
stats = stats(entry)
calculate(stats)

# entry: 361527
# wrong: 327 (too high)
# right: 326

# square = 3: max 2 steps, min 1 step
# square = 5: max 4 steps, min 2 steps
# square = 7: max 6 steps, min 3 steps
# square = 9: max 8 steps, min 4 steps

# 65 64 63 62 61 60 59 58 57
# 66 37 36 35 34 33 32 21 56
# 67 38 17 16 15 14 13 30 55
# 68 39 18  5  4  3 12 29 54
# 69 40 19  6  1  2 11 28 53
# 70 41 20  7  8  9 10 27 52
# 71 42 21 22 23 24 25 26 51
# 72 43 44 45 46 47 48 49 50
# 73 74 75 76 77 78 79 80 81
