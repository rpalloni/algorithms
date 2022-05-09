# Given an array of n distinct integers, transform the array into a zig-zag sequence
# by permuting the array elements. A sequence will be called a zig-zag sequence
# if the first k elements in the sequence are in increasing order and the last k elements
#  are in decreasing order, where k = (n + 1)/2

def find_zig_zag(arr, n):
    a = sorted(arr)
    mid = n // 2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return

arr = [3, 7, 4, 5, 9, 2, 12, 6]

find_zig_zag(arr, len(arr))
