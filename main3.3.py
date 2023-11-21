class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def can_visit_all_indices(strings):
    n = len(strings)
    dsu = DSU(n)

    for i in range(n):
        for j in range(i + 1, n):
            if hamming_distance(strings[i], strings[j]) == 1:
                dsu.union(i, j)

    root = dsu.find(0)
    return "YES" if all(dsu.find(i) == root for i in range(1, n)) else "NO"

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        strings = [input().strip() for _ in range(n)]
        result = can_visit_all_indices(strings)
        print(result)

if __name__ == "__main__":
    main()
