def solution(H):
    counter = 0
    stack = []
    for i in range(len(H)):
        while stack and stack[-1] > H[i]:
            stack.pop()
        if not stack or stack[-1] < H[i]:
            stack.append(H[i])
            counter += 1
    return counter

A = [8, 8, 5, 7, 9, 8, 7, 4, 8]
B = [0,1,0,0,0]