import sys

def solve():
    # so on day 0, only house 0 is infected
    # then each day exactly one neighboring house gets infected
    n, m, l, r = map(int, sys.stdin.readline().split())
    
    # and after m days, we have m+1 infected houses total -- counting the first one
    # in final state [l,r], we have -l left steps and r right steps
    total_left_steps = -l
    total_right_steps = r
    
    # lets distribute m steps in the same ratio as the final distribution
    if total_left_steps + total_right_steps == 0:  # avoid division by zero
        steps_left = m // 2
    else:
        steps_left = int(m * total_left_steps / (total_left_steps + total_right_steps))
    
    # remaining steps go to the right
    steps_right = m - steps_left
    
    # calculate the segment boundaries
    # going steps_left to the left, that is ---> -steps_left
    # and steps_right to the right is --> steps_right
    l_prime = -steps_left
    r_prime = steps_right
    
    print(l_prime, r_prime)

# no of test cases
t = int(sys.stdin.readline())
for _ in range(t):
    solve()