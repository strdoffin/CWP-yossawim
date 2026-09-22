#!/usr/bin/env python3

import sys

count = len(sys.argv[1:])
if count != 1:
    print("none")
    sys.exit()
text = ""
for i in sys.argv[1]:
    if i == 'z':
        text+=i
if text != '':
    print(text)
else:
    print("none")