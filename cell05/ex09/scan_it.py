#!/usr/bin/env python3
import sys
import re
num = len(sys.argv[1:])
if num != 2:
    print("none")
else:
    total = re.findall(sys.argv[1], sys.argv[2])
    if len(total) == 0:
        print("none")
        sys.exit()
    print(len(total))