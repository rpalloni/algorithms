'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''

def is_valid(s: str) -> bool:
    if s == '':
        return True
    left = []
    for a in s:
        if a in ['(', '[', '{']:
            left.append(a)
        elif not left or abs(ord(a)-ord(left[-1])) > 2:
            return False
        else:
            left.pop()
    if len(left) > 0:
        return False
    else:
        return True


f_string = '{[(])}'
t_string = '()[]{}'

is_valid(f_string)
is_valid(t_string)
