#Time Complexity O(Nlog(N))

def solution(N):

    for i in range(0,N):
        res = N - i
        if isSprase(i) and isSprase(res):
            return(i)
    return -1

def isSprase(N):
    binary_rep = bin(N)[2:]
    for i in range(0,len(binary_rep)-1):
        if binary_rep[i] == '1' and binary_rep[i+1] == '1':
            return False
    return True


#Time Complexity O(Nlog(N))
def solution(N):
    # Iterate through possible decompositions
    for i in range(0, N + 1):  # Include all possible numbers from 0 to N
        res = N - i
        if isSparse(i) and isSparse(res):
            return i  # Return the first valid sparse part
    return -1

def isSparse(N):
    # Check if the number is sparse using bitwise operations
    return (N & (N >> 1)) == 0
