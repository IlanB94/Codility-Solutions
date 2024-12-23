#Time Complexity O(N^2)
def solution(A):
    maxProfit = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] < A[j]:
                res = A[j] - A[i]
                maxProfit = max(maxProfit,res)
    return maxProfit

#Time Complexity O(N)
def solution(A):
    if not A:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        profit = price - min_price

        max_profit = max(max_profit, profit)

        min_price = min(min_price, price)

    return max_profit
