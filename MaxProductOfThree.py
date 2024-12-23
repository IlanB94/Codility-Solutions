# O(NlogN)

def solution(A):
    A.sort()
    print(A)
    if len(A) >= 3:
        max1 = A[-1] * A[-2] * A[-3]
        max2 = A[0] * A[1] * A[-1]
        return max(max1,max2)
    else:
        return -1