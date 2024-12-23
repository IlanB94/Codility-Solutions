def solution(X,A):
    my_set = set()
    for i,key in enumerate(A):
        if key <= X:
            my_set.add(key)
        if len(my_set) == X:
            return i

    return -1



A = [1,3,1,4,2,3,5,4]
print(solution(5,A))