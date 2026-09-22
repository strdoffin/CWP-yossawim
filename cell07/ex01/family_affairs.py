#!/usr/bin/env python3

def find_the_redheads(fam):
    arr = []
    for i in fam:
        if fam[i] == 'red':
            arr.append(i)
    return arr

dupont_family = {
    "florian" : "red",
    "marie" : "blond",
    "virginie" : "brunette",
    "david":"red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))