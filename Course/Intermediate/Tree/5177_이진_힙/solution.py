import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')



T = int(input())
for test_case in range(1,T+1):
    N = int(input())

    print('#{} {}'.format(test_case, b_tree[1]))