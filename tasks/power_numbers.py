'''
Given two integers, l and r, find the number of integers x such that l ≤ x ≤ r, and x is a Power Number.
A Power Number is defined as an integer that can be represented as sum of two powers, i.e.
x = a^p + b^q
a, b, p and q are all integers
a, b ≥ 0
p, q > 1

For example, given l=20 and r=25:
20 = 2^2 + 4^2
24 = 2^3 + 4^2
25 = 3^2 + 4^2
'''

def count_power_numbers(l, r):
    counter = 0
    n = [False]*(r+1)
    power_numbers = []
    n[1] = True

    for i in range(2, r):
        if pow(i, 2) >= r:
            break

        for j in range(2, r):
            if pow(i, j) >= r:
                break

            t = pow(i, j)
            n[t] = True

    for i in range(l, r):
        if n[i]:
            power_numbers.append(i)
            counter += 1
        else:
            for j in reversed(range(0, i-1)):
                if (n[j] and n[i-j]):
                    if i not in power_numbers:
                        power_numbers.append(i)
                        counter += 1

    print(power_numbers)
    return counter

count_power_numbers(25, 30)
