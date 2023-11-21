def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def can_visit_all_indices(strings):
    n = len(strings)
    for i in range(n):
        visited = set([i])
        current_index = i
        for _ in range(n - 1):
            next_index = None
            for j in range(n):
                if j not in visited and hamming_distance(strings[current_index], strings[j]) == 1:
                    next_index = j
                    break
            if next_index is None:
                break
            visited.add(next_index)
            current_index = next_index
        if len(visited) == n:
            return "YES"
    return "NO"

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        strings = [input().strip() for _ in range(n)]
        result = can_visit_all_indices(strings)
        print(result)

if __name__ == "__main__":
    main()
