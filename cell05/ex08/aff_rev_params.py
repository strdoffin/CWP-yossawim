#!/usr/bin/env python3
import sys

num = len(sys.argv[1:])
if num < 2:
    print("none")
else:
    arr = sys.argv[1:][::-1]
    for i in arr:
        print(i)