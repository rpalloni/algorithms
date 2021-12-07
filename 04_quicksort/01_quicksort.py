def partition(input_list, low, high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[i+1], input_list[high] = input_list[high], input_list[i+1]
    return (i+1)


def quick_sort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list, low, high)
        quick_sort(input_list, low, partition_index - 1)
        quick_sort(input_list, partition_index + 1, high)


input_list = [9, -3, 5, 2, 6, 8, -6, 1, 3]
input_len = len(input_list)

quick_sort(input_list, 0, input_len - 1)

print(input_list)
