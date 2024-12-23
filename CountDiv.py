# Time Complexity O(B-A)

# def solution(A, B, K):
#     counter =0
#     for i in range(A,B):
#         if i % K == 0:
#             counter += 1
#     return counter


# Time Complexity O(1)
def solution(A, B, K):
    # Count numbers divisible by K up to B
    divisible_up_to_B = B // K
    # Count numbers divisible by K up to A-1
    divisible_up_to_A_minus_1 = (A - 1) // K
    # Total count in range [A, B]
    return divisible_up_to_B - divisible_up_to_A_minus_1

A = 10
B = 10
K = 5
print(solution(A,B,K))