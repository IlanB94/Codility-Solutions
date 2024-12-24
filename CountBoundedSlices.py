def solution(K, A):
    counter =0
    sumP = 0
    minNum = 2**31-1
    maxNum = -2**31-1
    for q in range(0,len(A)):
        for p in range(q,len(A)):
            sumP = A[q] + A[p]
            maxNum = max(maxNum,sumP)
            minNum = min(minNum, sumP)
            if maxNum - minNum <= K:
                counter += 1
                print("(", q , "," , p ,")")
        minNum = 2**31-1
        maxNum = -2**31-1
    return counter




A = [3,5,7,6,3]
B = 2

print(solution(B,A))



