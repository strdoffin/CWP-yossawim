#!/usr/bin/env python3

print("Enter the first number:")
n1 = int(input())
print("Enter the second number:")
n2 = int(input())

result = n1 * n2
print(n1,"x",n2,"=",result)

if result == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is negative.")
