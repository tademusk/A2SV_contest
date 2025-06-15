def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        # The number of moves is the minimum number of 0s and 1s
        moves = min(s.count('0'), s.count('1'))
        # If the number of moves is odd, Alice wins; otherwise, Bob wins
        if moves % 2 == 1:
            print("DA")
        else:
            print("NET")

if __name__ == "__main__":
    solve() 