#!/usr/bin/env python3

import sys

count = len(sys.argv[1:])
if count < 1:
    print("none")
    sys.exit()
for i in sys.argv[1:]:
    if not i.endswith("ism"):
        print(i+"ism")
