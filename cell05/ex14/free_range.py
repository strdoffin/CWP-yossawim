#!/usr/bin/env python3

import sys

count = len(sys.argv[1:])
if count != 2:
    print("none")
    sys.exit()
start = int(sys.argv[1])
stop = int(sys.argv[2]) 
step = 1
if start > stop:
    step = -1
    stop -= 1
else:
    stop += 1
arr = []
for i in range(start, stop, step):
    arr.append(i)
print(arr)