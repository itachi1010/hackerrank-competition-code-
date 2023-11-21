MOD = 10**9 + 7

def solve(n):
    dp = [[0]*501 for _ in range(501)]
    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = 1
        for j in range(1, i+1):
            if i%2 == j%2:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    return sum(dp[n]) % MOD

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(solve(n))
