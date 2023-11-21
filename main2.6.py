def count_subsequences(N):
    mod = ((10**9) + 7)

    # Initialize the dp array with zeros
    dp = [0] * (N + 1)

    # Base case: there is one valid subsequence with only the first element
    dp[1] = 1

    # Iterate over the range from 2 to N (inclusive)
    for i in range(2, N + 1):
        # Calculate the number of valid subsequences ending with an odd number
        # and update the dp array
        dp[i] = (dp[i - 1] * 2) % mod

    # Calculate the final result by subtracting 1 and taking the modulo
    result = (dp[N] - 1) % mod

    return result

# Example usage:
N = 10
result = count_subsequences(N)
print(result)
