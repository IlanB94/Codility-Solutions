import math
#Time complexity O(sqrt(N)
def solution(N):
    minParaimeter = 2**31-1
    x = (int)(math.sqrt(N)) + 1
    for i in range(1,x):
        if N % i == 0:
            res = (int)(N / i)
            temp = 2 * (res + i)
            minParaimeter = min(minParaimeter,temp)
    return minParaimeter
