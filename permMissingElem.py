def solution(A):
    sum = 0
    arrayLength1 = len(A) + 1
    arrayLength2 = len(A) + 2
    x = (int)((arrayLength1 * arrayLength2)/2)
    for num in A:
        sum+=num
    return x-sum

A = [2,3,1,5]
print(solution(A))