def count_xor_pairs(n, arr, q, queries):
    # Function to count XOR pairs for a given range [l, r]
    def count_xor_pairs_in_range(l, r):
        count = 0
        for i in range(l, r):
            for j in range(i + 1, r):
                if arr[i] ^ arr[j] == 0:
                    count += 1
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
