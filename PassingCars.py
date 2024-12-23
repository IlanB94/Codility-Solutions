# Method 1 n^2
def solution(A):
    counter =0
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if (A[i] == 0 and A[j] == 1) and i < j:
                counter = counter+1
    return counter



# Method 2 n
def solution(A):
    count_east=0
    passing_cars =0
    for car in A:
        if car == 0:
            count_east+=1
        elif car == 1:
            passing_cars+=count_east
            if passing_cars > 1_000_000_000:
                return -1
    return passing_cars

A = [0,1,0,1,1]
print(solution(A))