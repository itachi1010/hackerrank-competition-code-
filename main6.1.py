MOD = 10**9 + 7

def dfs(s, i, x, y, target_x, target_y):
    if i == len(s):
        if x == target_x and y == target_y:
            return 1
        return 0
    if s[i] == '?':
        return (dfs(s, i+1, x+1, y, target_x, target_y) +
                dfs(s, i+1, x-1, y, target_x, target_y) +
                dfs(s, i+1, x, y+1, target_x, target_y) +
                dfs(s, i+1, x, y-1, target_x, target_y)) % MOD
    elif s[i] == 'R':
        return dfs(s, i+1, x+1, y, target_x, target_y) % MOD
    elif s[i] == 'L':
        return dfs(s, i+1, x-1, y, target_x, target_y) % MOD
    elif s[i] == 'U':
        return dfs(s, i+1, x, y+1, target_x, target_y) % MOD
    elif s[i] == 'D':
        return dfs(s, i+1, x, y-1, target_x, target_y) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    target_x, target_y = map(int, input().split())
    print(dfs(s, 0, 0, 0, target_x, target_y) % MOD)
