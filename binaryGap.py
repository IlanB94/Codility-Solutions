def solution(N):
    binary_representation =  bin(N)[2:]
    gap =0
    maxGap =0
    for char in binary_representation:
        if char == '1':
            maxGap = max(maxGap,gap)
            gap =0
        else:
            gap = gap + 1

    return maxGap


print(solution(5))