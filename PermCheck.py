

def solution(A):
    my_set = set()
    for num in A:
        if not(num in my_set):
            my_set.add(num)
    x = len(my_set)
    if len(my_set) == len(A) and max(A) == len(A):
        return 1

    return 0

A = [4,1,3,2]
print(solution(A))