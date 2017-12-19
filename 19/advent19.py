import sys
import re

def read_file():
  file = sys.argv[1]
  return [line.strip('\n') for line in open(file).readlines()]

p = re.compile('[A-Z]')
def match(path, found):
  return p.match(found) or path == found

def is_left(maze, y, current_x):
  if current_x - 1 < 0:
    return False
  return maze[y][current_x - 1] != ' '

def is_up(maze, x, current_y):
  if current_y - 1 < 0:
    return False
  return maze[current_y - 1][x] != ' '

maze = read_file()
x = maze[0].index('|')
y = 1
x_dir = 0
y_dir = 1
seen = []
count = 1
while True:
  next = maze[y][x]
  if next == ' ':
    break
  elif p.match(next):
    seen.append(next)
  elif next == '+':
    if y_dir != 0:
      y_dir = 0
      if is_left(maze, y, x):
        x_dir = -1
      else:
        x_dir = 1
    elif x_dir != 0:
      x_dir = 0
      if is_up(maze, x, y):
        y_dir = -1
      else:
        y_dir = 1
    else:
      break
  count += 1
  y += y_dir
  x += x_dir

print(''.join(seen))
print("Count: " + str(count))