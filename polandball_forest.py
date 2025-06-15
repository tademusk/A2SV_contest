def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root


def solve():
    n = int(input())
    p = list(map(int, input().split()))
    parent = list(range(n))
    for i in range(n):
        # Union i and p[i]-1 (convert to 0-based)
        union(parent, i, p[i] - 1)
    # Count unique roots
    roots = set(find(parent, i) for i in range(n))
    print(len(roots))

if __name__ == "__main__":
    solve() 