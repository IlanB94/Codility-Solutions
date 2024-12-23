def solution(S):
    stack = []
    for char in S:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 0
            stack.pop()

    if not stack:
        return 1
    else:
        return 0

A = "(()"
B = [0,1,0,0,0]