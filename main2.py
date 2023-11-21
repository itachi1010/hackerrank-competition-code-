MOD = 10 ** 9 + 7


def count_subsequences(t, n_values):
    results = []

    for N in n_values:
        # Initialize counts for subsequences ending with odd and even numbers
        odd_count = 1
        even_count = 1

        # Calculate counts for subsequences
        for i in range(2, N + 1):
            if i % 2 == 1:
                odd_count = (2 * odd_count) % MOD
            else:
                even_count = (2 * even_count) % MOD

        # Total count of valid subsequences
        result = (odd_count + even_count) % MOD
        results.append(result)

    return results


# Specific use case: 2 test cases
t = 2
# N values for each test case
n_values = [4, 10]

# Calculate and print the results
results = count_subsequences(t, n_values)
for result in results:
    print(result)
