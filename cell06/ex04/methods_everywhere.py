#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])
def enlarge(text):
    z = 8 - len(text)
    print(text + (z*"Z"))

if len(sys.argv[1:]) < 1:
    print("none")
    sys.exit()

for i in sys.argv[1:]:
    if len(i) <= 8:
        enlarge(i)
    else:
        shrink(i)