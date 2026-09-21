#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
n_arr = []
for i in range(0,len(arr)):
    if arr[i] > 5:
        n_arr.append(arr[i]+2)
print(arr)
print(set(n_arr))