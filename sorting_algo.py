def merge_sort(array: list[int]) -> list[int]:
    """Sort a given list of int using merge sort algorithm
    Source: https://www.programiz.com/dsa/merge-sort

    Args:
        array (int): An array that want to be sorted
    """
    if len(array) > 1:

        #  mid is the point where the array is divided into two subarrays
        mid = len(array)//2
        left_half = array[:mid]
        right_half = array[mid:]

        # Sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Until we reach either end of either left_half or right_half, pick larger among
        # elements left_half and right_half and place them in the correct position at A[p..r]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
