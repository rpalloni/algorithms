

def subarray_sum(arr):
    temp, result = 0, 0
    n = len(arr)

    # Pick starting point
    for i in range(0, n):

        # Pick ending point
        temp = 0
        for j in range(i, n):

            # sum subarray between
            # current starting and
            # ending points
            temp += arr[j]
            result += temp
    return result

a = [1, 2, 3]
subarray_sum(a)


# Given an array of positive and negative numbers,
# find if there is a subarray (of size at-least one) with 0 sum.


def subarray_sum_zero(arr):
    n = len(arr)
    n_sum = 0
    s = set()
    for i in range(n):
        n_sum += arr[i]
        print(arr[i])
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
        print(s)
    return False

# subarray with element zero (a single element is also a subarray)
a0 = [4, 2, 0, 1, 6]
subarray_sum_zero(a0)

# subarray with zero sum from index 1 to 3
a1 = [4, 2, -3, 1, 6]
subarray_sum_zero(a1)

# no subarray with zero sum
a2 = [-3, 2, 3, 1, 6]
subarray_sum_zero(a2)
