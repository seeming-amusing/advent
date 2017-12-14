import sys
import time as t

class Sensor:
  def __init__(self, range):
    self.range = range
    self.position = 1 if range > 0 else 0
    self.direction = 1

  def __repr__(self):
    return "S (pos: " + str(self.position) + ")"

  def is_caught(self, time):
    if self.range == 0:
      return False
    return time % (2 * (self.range - 1)) == 0

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.readlines()
  return content

def extractFirewall():
  file = readFile()
  firewall = dict()
  for line in file:
    vals = [int(v) for v in line.rstrip('\n').split(': ')]
    firewall[vals[0]]  = Sensor(vals[1])
  return firewall

def find_severity(firewall):
  severity = 0
  for i, sensor in firewall.iteritems():
    if firewall[i].is_caught(i):
      severity += i * firewall[i].range
  return severity

def is_caught(firewall, delay):
  for i, sensor in firewall.iteritems():
    if sensor.is_caught(i + delay):
      return True
  return False

firewall = extractFirewall()
print find_severity(firewall)
delay = 0
start = t.time()
while is_caught(firewall, delay):
  delay += 1
print "Wait " + str(delay) + " ps"
print "Completed in " + str(t.time() - start) + " s"