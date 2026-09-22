#!/usr/bin/env python3
import sys

num = len(sys.argv[1:])
if num == 0:
    print("none")
else:
    print(sys.argv[1])