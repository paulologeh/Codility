# Write a function:


# def solution(A)


# that, given an array A of N integers, returns the smallest positive integer(greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range[1..100, 000]
# each element of array A is an integer within the range[−1, 000, 000..1, 000, 000].

def solution(A):
    # write your code in Python 3.6
    maxVal = 0
    for val in A:
        if val > maxVal:
            maxVal = val

    if maxVal == 0:
        return 1

    arr = [0] * maxVal

    for val in A:
        if val > 0:
            arr[val-1] = val

    for i, value in enumerate(arr):
        if value == 0:
            return i + 1

    return maxVal + 1
