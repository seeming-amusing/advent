class Generator:
  def __init__(self, factor, critera, start):
    self.factor = factor
    self.critera = critera
    self.value = start
  def next(self):
    self.value = (self.factor * self.value) % divisor
    while self.value % self.critera != 0:
      self.value = (self.factor * self.value) % divisor
    return '{0:032b}'.format(self.value)

divisor = 2147483647

def part_1():
  a = Generator(16807, 1, 703)
  b = Generator(48271, 1, 516)
  duel(a, b, 40_000_000)

def part_2():
  a = Generator(16807, 4, 703)
  b = Generator(48271, 8, 516)
  duel(a, b, 5_000_000)

def duel(a, b, times):
  matches = 0
  for i in range(times):
    if a.next()[16:] == b.next()[16:]:
      matches += 1
  print(matches)

part_1()
part_2()