import sys

def readFile():
  fileName = sys.argv[1]
  with open(fileName) as f:
    content = f.readlines()
  return [line.rstrip('\n').split(' ') for line in content]

def is_valid(words):
  word_set = set()
  for word in words:
    if word in word_set:
      return False
    word_set.add(word)
  return True

def find_valid_passphrases(passphrases):  
  valid_passphrases = 0
  for words in passphrases:
    if is_valid([''.join(sorted(word)) for word in words]):
      valid_passphrases += 1
  print str(valid_passphrases) + " out of " + str(len(passphrases))

passphrases = readFile()
find_valid_passphrases(passphrases)