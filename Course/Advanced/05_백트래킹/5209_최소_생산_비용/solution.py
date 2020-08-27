import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

def dfs(start):


T = int(input())
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]

    print('#{} {}'.format(test_case, dfs(1)))
