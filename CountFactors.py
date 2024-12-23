# Time Complexity O(N)
import math


def solution(N):
    counter = 0
    for i in range(1,N+1):
        if N % i == 0:
            counter += 1
    return counter


#Time Complexity O(√N)
def solution(N):
    counter = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            counter += 1
            if i != N // i:
                counter += 1
    return counter
