# time complexity of the solution is O(m*n)
# space complexity is O(m*n)

def isMatch(s, p):

    rows, columns = (len(s), len(p))
    # Base conditions
    if rows == 0 and columns == 0:
        return True
    if (columns == 0 and rows != 0) or (rows == 0 and columns != 0):
        return False
    
    # fill a 2d array
    dp = [[False for j in range(columns + 1)] for i in range(rows + 1)]
    dp[0][0] = True

    #validation using DP
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '+':
                if (p[j - 2] == '.') or (p[j - 2] == s[i - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
    return dp[rows][columns]

# keep this function call here 
print(isMatch("abcdef", "a.+.+"))