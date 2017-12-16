import sys

def read_file():
  file = sys.argv[1]
  return list(map(int, open(file).read().rstrip('\n').split(',')))

vals = list(range(256))
size = len(vals)
lengths = read_file()
i = 0
skip_size = 0
for l in lengths:
  full_l = l + i
  last_i = full_l if full_l < size else size
  looped_i = 0 if full_l < size else full_l - size
  sublist = vals[i:last_i] + vals[0:looped_i]
  sublist.reverse()
  if looped_i == 0:
    vals[i:last_i] = sublist
  else:
    vals[i:last_i] = sublist[0:last_i - i]
    vals[0:looped_i] = sublist[last_i - i:]
  i = (i + l + skip_size) % size
  skip_size += 1

print(vals)
print(vals[0] * vals[1])