def solution(A):
    leftSum=0
    rightsum = 0
    arraySum =0
    minimunSum = 2**31 - 1
    for i in range(0,len(A)):
        arraySum += A[i]
    for i in range(0,len(A)):
        leftSum += A[i]
        rightsum = arraySum-leftSum
        sum = abs(leftSum - rightsum)
        minimunSum = min(minimunSum,sum)
    return minimunSum
A = [3]
print(solution(A))