#Time complexity O(N^2)

def solution(A):
    counter = 0
    arr = []
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i != j and A[i] % A[j] != 0:
                counter += 1
        arr.append(counter)
        counter = 0
    return arr



A = [3,1,2,3,6]

print(solution(A))

