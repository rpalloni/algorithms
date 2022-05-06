# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.


def first_unique_char(s):
    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    c = [0] * 26
    for i in s:
        c[ord(i) - ord('a')] += 1
    print(c)
    for index, i in enumerate(s):
        if c[ord(i) - ord('a')] == 1:
            return index
    return -1

first_unique_char('pippo') # "i" at index 1


#Note ASCII domain:
ord('a')
chr(97)

ord('p') - ord('a')
ord('i') - ord('a')
ord('p') - ord('a')
ord('p') - ord('a')
ord('o') - ord('a')

for index, i in enumerate('pippo'):
    print(index, i)
