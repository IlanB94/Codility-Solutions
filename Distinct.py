#Time Complexity O(n)

def solution(A):
    mySet = set()
    for num in A:
        if not(mySet.__contains__(num)):
            mySet.add(num)
    return len(mySet)

A = (2,1,1,2,3,1)
print(solution(A))