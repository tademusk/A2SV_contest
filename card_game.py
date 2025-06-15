def solve():
    t = int(input())
    for _ in range(t):
        n, k1, k2 = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        # The player with the highest card overall will always win if playing optimally
        if max(a) > max(b):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve() 