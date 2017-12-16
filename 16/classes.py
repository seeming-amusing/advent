def parse(move):
  if move[0] == 's':
    return Spin(move)
  elif move[0] == 'x':
    return Exchange(move)
  elif move[0] == 'p':
    return Partner(move)

class Spin:
  def __init__(self, move):
    self.num = int(move[1:])
  def __repr__(self):
    return "spin " + str(self.num)
  def dance(self, dancers):
    return dancers[-self.num:] + dancers[:-self.num]

class Exchange:
  def __init__(self, move):
    self.a, self.b = map(int, move[1:].split('/'))
  def __repr__(self):
    return "exchange " + str(self.a) + " <-> " + str(self.b)
  def dance(self, dancers):
    dancers[self.a], dancers[self.b] = dancers[self.b], dancers[self.a]
    return dancers

class Partner:
  def __init__(self, move):
    self.a, self.b = move[1:].split('/')
  def __repr__(self):
    return "partner " + str(self.a) + " <-> " + str(self.b)
  def dance(self, dancers):
    a, b = dancers.index(self.a), dancers.index(self.b)
    dancers[a], dancers[b] = dancers[b], dancers[a]
    return dancers