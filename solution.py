

def solution(H):
    counter = 0
    stack = []
    for height in H:
        while stack and stack[-1] > height:
            stack.pop()
        if not stack or stack[-1] < height:
            stack.append(height)
            counter += 1
    return counter






A = [8, 8, 5, 7, 9, 8, 7, 4, 8]
B = [0,1,0,0,0]

print(solution(A))