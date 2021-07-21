def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        print(array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')