grid = [0]
step = 304
until = 2017
position = 0
for i in range(until):
  position = ((step + position) % len(grid)) + 1
  grid.insert(position, (i + 1))
print(grid[position + 1])

i = 0
for t in range(1, 50_000_001):
  i = ((i + step) % t) + 1
  if i == 1:
    found = t
print(found)