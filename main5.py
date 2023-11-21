def count_xor_pairs(n, arr, q, queries):
    # Compute the prefix XOR array
    prefix_xor = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

    # Function to count XOR pairs for a given range [l, r]
    def count_xor_pairs_in_range(l, r):
        xor_dict = {}  # Dictionary to store XOR values and their counts
        count = 0
        for i in range(r, l, -1):
            current_xor = prefix_xor[i - 1]
            count += xor_dict.get(current_xor, 0)
            xor_dict[prefix_xor[i]] = xor_dict.get(prefix_xor[i], 0) + 1

        return count

    # Process each query and print the result
    for query in queries:
        l, r = query
        result = count_xor_pairs_in_range(l - 1, r)
        print(result)

# Read input
n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

# Call the function with the given input
count_xor_pairs(n, arr, q, queries)
