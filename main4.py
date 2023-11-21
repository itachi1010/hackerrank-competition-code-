def generate_string(Na, Nb, Sa, Sb, K):
    S = ""
    current_count = 1

    while True:
        if current_count % Na == 0 and current_count % Nb == 0:
            S += Sa + Sb
        elif current_count % Na == 0:
            S += Sa
        elif current_count % Nb == 0:
            S += Sb

        if len(S) >= K:
            return S[K - 1]

        current_count += 1

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read input for each test case
    Na, Nb = map(int, input().split())
    Sa = input().strip()
    Sb = input().strip()
    K = int(input())

    # Generate and print the result for the current test case
    result = generate_string(Na, Nb, Sa, Sb, K)
    print(result)
