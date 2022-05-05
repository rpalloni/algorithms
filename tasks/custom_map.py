# improve map generator to map a series of functions over an input
# it takes as input a list of functions and a list of integers
# For example, funcs = [lambda x:x*x, lambda x:x+x] and arr = [1,2,3,4]
# and returns [2,8,18,32], i.e. [1,4,9,16]=>[2,8,18,32]

import types

def cmap(funcs, arr):
    for f in funcs:
        output = list(map(f, arr))
        arr = output
        yield output # generator required


# funcs = [lambda x: x*x, lambda x: x+x]
# arr = [1, 2, 3, 4]

# result = cmap(funcs, arr)
# for result_item in result:
#     print(result_item)


# test
test = {
    'input': {
        'array': [1, 2, 3, 4],
        'funcs': [lambda x: x*x, lambda x: x+x]
    },
    'output': [[1, 4, 9, 16], [2, 8, 18, 32]]
}

assert(isinstance(cmap(test['input']['funcs'], test['input']['array']), types.GeneratorType)) == True
next(cmap(test['input']['funcs'], test['input']['array'])) == test['output'][0]
next(cmap(test['input']['funcs'], test['input']['array'])) == test['output'][1]
