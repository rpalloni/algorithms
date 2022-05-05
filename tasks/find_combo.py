# Given two integers n and r how many ways can r items be chosen from n items?
# nCr = (n!) / (r! * (n-r)!)
# where n! = product of all positive integers <= n (e.g. 5! = 5*4*3*2*1 = 120)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nCr(n, r):
    return (factorial(n) / (factorial(r) * factorial(n - r)))


nCr(2, 1)
nCr(4, 0)
nCr(5, 2)
nCr(10, 3)
