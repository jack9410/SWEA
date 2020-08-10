import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


def makeTree(n):
    global count
    if n <= N:
        makeTree(n*2)
        b_tree[n] = count
        count += 1
        makeTree(n*2 + 1)


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    b_tree = [0 for i in range(N+1)]
    count = 1
    makeTree(1)

    print('#{} {} {}'.format(test_case, b_tree[1], b_tree[N//2]))