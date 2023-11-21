def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def dfs(graph, visited, node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor)


def can_visit_all_indices(strings):
    n = len(strings)
    graph = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if i != j and hamming_distance(strings[i], strings[j]) == 1:
                graph[i].append(j)

    for i in range(n):
        visited = set()
        dfs(graph, visited, i)
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
