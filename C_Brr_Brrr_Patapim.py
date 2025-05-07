import sys

def solve():
    n = int(sys.stdin.readline())

    # using 1-based indexing for p, size 2n+1
    p = [0] * (2 * n + 1)
    seen_values = set()

    # read the grid and fill p[2]...p[2n]
    for i in range(1, n + 1):
        row_values = list(map(int, sys.stdin.readline().split()))
        for j in range(1, n + 1):
            # 0-based index for row_values
            grid_value = row_values[j-1] 
            k = i + j
            p[k] = grid_value
            seen_values.add(grid_value)

    # find p[1] -->the missing value
    all_possible_values = set(range(1, 2 * n + 1))
    p1 = (all_possible_values - seen_values).pop()
    p[1] = p1

    
    print(*p[1:])

#  no of test cases
t = int(sys.stdin.readline())

for _ in range(t):
    solve()