import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

for test_case in range(1,11):
    N = int(input())
    line = list(map(int, input().split('+')))
    # print(line)
    print('#{} {}'.format(test_case, sum(line)))