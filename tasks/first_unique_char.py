# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.


def first_unique_char(s):
    """
    :type s: str
    :rtype: int
    """
    c = [0] * 26
    for i in s:
        c[ord(i) - ord('a')] += 1
    for index, i in enumerate(s):
        if c[ord(i) - ord('a')] == 1:
            return index
    return -1

first_unique_char('pippo')
