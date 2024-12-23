def solution(A, B):
    downstreamStack = []
    survivors = 0
    for i in range(len(A)):
        if B[i] == 1:
            downstreamStack.append(A[i])
        else:
            while downstreamStack and downstreamStack[-1] < A[i]:
                downstreamStack.pop()
            if not downstreamStack:
                survivors += 1
    return survivors + len(downstreamStack)


A = [4,3,2,1,5]
B = [0,1,0,0,0]