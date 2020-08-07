import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    N,M,K = map(int, input().split())
    pwd = list(map(int, input().split()))
    # print(pwd)

    idx = 0
    for _ in range(K):
        idx += M
        if idx == len(pwd):
            pwd.append(pwd[-1] + pwd[0])
        elif idx > len(pwd)-1:
            idx %= len(pwd)
            pwd.insert(idx, pwd[idx-1] + pwd[idx] )
        else:
            pwd.insert(idx, pwd[idx-1] + pwd[idx] )
        # print(pwd)

    print('#{} {}'.format(test_case, ' '.join(map(str, pwd[-1:-11:-1]))))