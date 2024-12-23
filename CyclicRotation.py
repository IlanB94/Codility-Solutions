def solution(A, K):
    N = len(A)
    a = [0] * N
    if N == K:
        return A
    for i in range(0,N):
        a[(K + i)%N] = A[i]

    return a

a = [3, 8, 9, 7, 6]
k = 3
print(solution(a,k))