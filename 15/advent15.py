divisor = 2147483647

def part_1():
  a = generator(16807, 1, 703)
  b = generator(48271, 1, 516)
  duel(a, b, 40_000_000)

def part_2():
  a = generator(16807, 4, 703)
  b = generator(48271, 8, 516)
  duel(a, b, 5_000_000)

def duel(a, b, times):
  matches = 0
  for i in range(times):
    if next(a) == next(b):
      matches += 1
  print(matches)

def generator(factor, critera, value):
  while True:
    value = (value * factor) % divisor
    if value % critera == 0:
      yield value & 0xffff

part_1()
part_2()