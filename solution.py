

def solution(A):
    maxProfit = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] < A[j]:
                res = A[j] - A[i]
                maxProfit = max(maxProfit,res)
    return maxProfit



A = [23171,21011,21123,21366,21013,21367]
B = [0,1,0,0,0]

print(solution(A))