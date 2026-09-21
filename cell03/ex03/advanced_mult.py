#!/usr/bin/env python3

import sys
def main():
    argc = len(sys.argv)
    if argc > 1:
        if sys.argv[1] == "yolo":
            print("none")
            return 0;

    i = 0
    while i != 11:
        j = 0
        num = 0
        print("Table de",i,":",end=" ")
        text = ""
        while j != 11:
            text += str(num)+" "
            num+=i
            j+=1
        print(text.rstrip(" "))
        i+=1

main()