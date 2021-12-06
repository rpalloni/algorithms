'''
The two key elements of a recursive algorithm are:
1) The termination condition: n == 0
2) The reduction step where the function calls itself with a smaller number each time: factorial(n - 1)
'''

import sys
sys.getrecursionlimit()

def recursive(string, num):
    if num < 10: # recursion limit
        print(f'{string} - {num}')
        recursive(string, num+1)

recursive("Hello world", 0)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(4)
