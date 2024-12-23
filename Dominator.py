def solution(A):
    if not A:
        return -1

    count_dict = {}
    for num in A:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    half_length = len(A)//2
    for num,count in count_dict.items():
        if count > half_length:
            return A.index(num)

    return -1

A = [3,4,3,2,3,-1,3,3]
