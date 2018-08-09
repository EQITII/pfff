#!/usr/bin/python3

import sys, subprocess
from functools import reduce

if len(sys.argv) < 2:
    print(sys.argv[0], '<file...>')
    sys.exit(2)

files = sys.argv
files.pop(0)

result = subprocess.run(['./build/src/pfff', '-B'] + files, stdout=subprocess.PIPE)
resultString = result.stdout.decode('utf-8')

hashes = list(filter(lambda s: len(s), resultString.split('\n')))
for hash in hashes:
    print(hash)

if len(hashes) > 1:
    areEqual = reduce(lambda a, b: a == b, hashes)
    print('Equal:', areEqual)