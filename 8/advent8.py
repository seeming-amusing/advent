import sys

class Instruction(object):
  def __init__(self, operation, evaluator):
    self.operation = operation
    self.evaluator = evaluator

class Operation:
  def __init__(self, reg, op, val):
    self.reg = reg
    self.op = op
    self.val = int(val)

  def invoke(self, register):
    init_if_necessary(register, self.reg)
    if self.op == 'inc':
      register[self.reg] += self.val
    elif self.op == 'dec':
      register[self.reg] -= self.val
    else:
      raise ValueError("Unknown operation")

class Evaluator:
  def __init__(self, reg, op, val):
    self.reg = reg
    self.op = op
    self.val = int(val)

  def invoke(self, register):
    init_if_necessary(register, self.reg)
    if self.op == '>':
      return register[self.reg] > self.val
    if self.op == '<':
      return register[self.reg] < self.val
    if self.op == '>=':
      return register[self.reg] >= self.val
    if self.op == '<=':
      return register[self.reg] <= self.val
    if self.op == '==':
      return register[self.reg] == self.val
    if self.op == '!=':
      return register[self.reg] != self.val
    else:
      raise ValueError("Unknown operation")

def init_if_necessary(register, key):
  if key not in register.keys():
    register[key] = 0

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.readlines()
  return [parse(line.rstrip('\n')) for line in content]

def parse(line):
  line = line.split(" if ")
  (op_reg, op, op_val) = line[0].split(' ')
  (ev_reg, ev, ev_val) = line[1].split(' ')
  return Instruction(Operation(op_reg, op, op_val), Evaluator(ev_reg, ev, ev_val))

register = dict()
instructions = readFile()
max_val = 0
for i in instructions:
  if (i.evaluator.invoke(register)):
    i.operation.invoke(register)
    if max(register.values()) > max_val:
      max_val = max(register.values())
print max(register.values())
print max_val