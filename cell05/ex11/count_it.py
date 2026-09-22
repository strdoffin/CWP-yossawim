#!/usr/bin/env python3

import sys

count = len(sys.argv[1:])
if count == 0:
    print("none")
else:
    print("parameters: ",count)
    for i in sys.argv[1:]:
        print(f"{i}: {len(i)}")