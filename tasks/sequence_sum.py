# Given three integers, i, j, and k, calculate the sequence sum to be the value of
# incrementing from i until it equals j, then decrement from j until it equals k.
# For example, i = 5, j = 9, k = 6 than sum all the values from i to j and back to k:
# 5 + 6 + 7 + 8 + 9 + 8 + 7 + 6 = 56

# using range step
def getSequenceSum(i, j, k):
    s = 0
    if i <= j:
        s += sum(i for i in range(i, j, 1))
    else:
        s += sum(i for i in range(i, j, -1))
    if j <= k:
        s += sum(j for j in range(j, k, 1))
    else:
        s += sum(j for j in range(j, k, -1))
    return s + k

getSequenceSum(5, 9, 6) # 56

getSequenceSum(0, 5, -1) # 24

getSequenceSum(8, 2, 7) # 60


# arithmetic progression: s = elements * (first+last)/2
def getSequenceSum(i, j, k):
    cnt_inc = j - i + 1
    cnt_dec = j - k + 1
    inc_sum = (cnt_inc * (i + j)) // 2
    dec_sum = (cnt_dec * (j + k)) // 2
    tot_sum = inc_sum + dec_sum - j
    return tot_sum

getSequenceSum(5, 9, 6) # 56

getSequenceSum(0, 5, -1) # 24

getSequenceSum(8, 2, 7) # error!
