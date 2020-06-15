def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Set boundaries for low and high marks to search

    low = 0
    high = len(arr)

    # While low and high don't overlap

    while low < high:
        # Check midpoint
        mid = (low + high) // 2
    # Return true if equal
        if arr[mid] == target:
            return mid
    # Else, if target is smaller, set high to midpoint value
        elif target < arr[mid]:
            high = mid
    # Else, if target is bigger, set low to modpoint value
        else:
            low = mid + 1

    return -1  # not found
