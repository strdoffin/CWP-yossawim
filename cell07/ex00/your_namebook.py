#!/usr/bin/env python3

def array_of_names(p):
    arr = []
    for i in p:
        name = f"{i.capitalize()} {p[i].capitalize()}"
        arr.append(name)
    return arr

persons = {
    "jean":"valjean",
    "grace":"hopper",
    "xavier":"niel",
    "fifi":"brindacier"
}

print(array_of_names(persons))