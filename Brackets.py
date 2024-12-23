

def solution(S):
    stack = []
    for char in S:
        if len(stack) == 0 or char not in (')','}',']'):
            stack.append(char)
        elif stack[-1] == '(' and char == ')':
            stack.pop()
        elif stack[-1] == '{' and char == '}':
            stack.pop()
        elif stack[-1] == '[' and char == ']':
            stack.pop()
    if len(stack) == 0:
        return 1
    return 0



A = "{[()()]}"
print(solution(A))