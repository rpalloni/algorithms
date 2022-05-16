'''calculate distance between two points (not orthogonal)'''

def distance_points(p1, p2):
    s1 = abs(p2[0] - p1[0])
    s2 = abs(p2[1] - p1[1])

    return s1 + s2

p1 = [0, 0]
p2 = [2, 2]

distance_points(p1, p2)


test = {
    'input': {
        'p1': [0, 0],
        'p2': [2, 2]
    },
    'output': 4
}

distance_points(test['input']['p1'], test['input']['p2']) == test['output']


test1 = {
    'input': {
        'p1': [1, 1],
        'p2': [2, 2]
    },
    'output': 2
}

distance_points(test1['input']['p1'], test1['input']['p2']) == test1['output']


test2 = {
    'input': {
        'p1': (2, 2),
        'p2': (1, 1)
    },
    'output': 2
}


distance_points(test2['input']['p1'], test2['input']['p2']) == test2['output']
