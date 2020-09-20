# Write a function:


# def solution(A, B, K)


# that, given three integers A, B and K, returns the number of integers within the range[A..B] that are divisible by K, i.e.:

# {i: A ≤ i ≤ B, i mod K = 0}

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range[6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range[0..2, 000, 000, 000]
# K is an integer within the range[1..2, 000, 000, 000]
# A ≤ B.

def solution(A, B, K):
    # write your code in Python 3.6
    if A == 0:
        A = A
    elif K <= A:
        C = A % K
        A = A + C
    else:
        A = K

    if B == 0:  # special case
        return 1

    if A > B:
        return 0
    elif A == B:
        return 1
    else:
        D = (B - A) // K
        return D + 1
