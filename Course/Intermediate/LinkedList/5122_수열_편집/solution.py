import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))

    for _ in range(M):
        cmd = list(map(str, input().split()))
        if cmd [0] == 'I':
            lst.insert(int(cmd[1]), cmd[2])
        elif cmd [0] == 'D':
            lst.pop(int(cmd[1]))
        elif cmd [0] == 'C':
            lst[int(cmd[1])] = cmd[2]
    
    # print(lst)
    if L > len(lst)-1:
        answer = -1
    else:
        answer = lst[L]

    print('#{} {}'.format(test_case, answer))