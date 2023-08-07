# LIS

list_a = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]

def lis_length(arr):
    n = len(arr)
    if n == 0:
        return 0

    # list initialized at 1
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # runs in O(n^2) time
    return max(dp)

print(lis_length(list_a))