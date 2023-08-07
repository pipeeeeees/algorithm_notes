# LIS

list_a = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]

def lis_length(arr):
    n = len(arr)
    if n == 0:
        return 0

    # list initialized at LIS = 1 for all
    dp = [1] * n

    # run through every combination of increasing subsequences and store only the greater incs length
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # return the greatest magnitude
    # runs in O(n^2) time
    return max(dp)

print(lis_length(list_a))