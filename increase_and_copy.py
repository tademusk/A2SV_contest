import math

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = n - 1
        sq = int(math.isqrt(n)) + 2
        # Try all k (number of elements after copying)
        for k in range(1, sq):
            x = (n + k - 1) // k
            moves = (x - 1) + (k - 1)
            if moves < ans:
                ans = moves
        # Try all x (value to increase to)
        for x in range(1, sq):
            k = (n + x - 1) // x
            moves = (x - 1) + (k - 1)
            if moves < ans:
                ans = moves
        print(ans)

if __name__ == "__main__":
    solve() 