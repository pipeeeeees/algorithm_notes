# LCS

"""
input: 2 strings
goal: find the length of the longest string which is a subsequence of both X & Y

example:
X = 'BCDBCDA'
Y = 'ABECBAB'
ANS = 4  #'BCBA'

this is applicable for unix diff
"""


X = 'BCDBCDA'
Y = 'ABECBAB'

def lcs_length(text1, text2):
    m, n = len(text1), len(text2)

    # 2 dimensional table initialized at 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # two indicies
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # O(n*m) time
    return dp[m][n]

print(lcs_length(X, Y))