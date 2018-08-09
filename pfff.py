#!/usr/bin/python3

import sys, subprocess
from functools import reduce

arguments = sys.argv
arguments.pop(0)

result = subprocess.run(['./build/src/pfff'] + arguments, stdout=subprocess.PIPE)
resultString = result.stdout.decode('utf-8')
print(resultString)
