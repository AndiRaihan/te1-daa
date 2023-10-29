import numpy as np


def merge_sort(array: list[int], *args, **kwargs) -> list[int]:
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

def two_pivot_block_partitioning(array: list[int], start: int, end: int, block_size: int) -> tuple[int, int]:
    """Returns two pivot index that divide the array into three parts using block partitioning method

    Args:
        array (list[int]): Array that will be partitioned
        start (int): The start of the partition
        end (int): The end of the partition
        block_size (int): The size of the block

    Returns:
        tuple[int, int]: A tuple of the first and second pivot index
    """
    if (end <= start):
        return (start, start)
    pivot1 = array[start]
    pivot2 = array[end]
    
    if (pivot1 > pivot2):
        array[start], array[end] = array[end], array[start]
        pivot1, pivot2 = pivot2, pivot1
    
    block = [None] * block_size
    
    i, j, k = start + 1, start + 1, start + 1
    nump, numq = 0, 0
    
    while k < end:
        t = min(block_size, end - k)
        for c in range(t):
            block[numq] = c
            numq = numq + (pivot2 >= array[k + c])
        for c in range(numq):
            array[j+c], array[k+block[c]] = array[k+block[c]], array[j+c]
        k += t
        for c in range(numq):
            block[nump] = c
            nump += (pivot1 > array[j + c])
        for c in range(nump):
            array[i], array[j + block[c]] = array[j + block[c]], array[i]
            i += 1
        j += numq
        nump, numq = 0, 0
    
    array[i-1], array[start] = array[start], array[i-1]
    array[j], array[end] = array[end], array[j]
    return (i-1, j)

def two_pivot_block_quicksort(array: list[int], start: int, end: int) -> None:
    if (len(array) == 0):
        return array
    
    # Berdasarkan paper, untuk data ukuran 2^26 block size yang optimal adalah 2^10. Saya simpulkan
    # bahwa untuk data ukuran 2^n, block size yang optimal adalah 2^(floor(n/3) + 2)
    block_size = np.log2(len(array))
    block_size = int(2 ** (np.floor(block_size) // 3 + 2))
    
    # Dibuat iteratif karena untuk data yang terlalu besar, akan terjadi stack overflow
    stack = [(start, end)]
    while stack:
        start, end = stack.pop()
        if start < end:
            pivots = two_pivot_block_partitioning(array, start, end, block_size)
            stack.extend([(start, pivots[0] - 1), (pivots[0] + 1, pivots[1] - 1), (pivots[1] + 1, end)])