import os
import sys
curr_dir = os.path.dirname(__file__)
# os.chdir(curr_dir)
sys.stdin = open(curr_dir + '\input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # print(N, M)
    first_lst = list(map(int, input().split()))
    # print(first_lst)

    for _ in range(M - 1):
        tmp_lst = list(map(int, input().split()))
        # print(tmp_lst)
        for i in range(len(first_lst)):
            # print(i, tmp_lst[0])
            if first_lst[i]> tmp_lst[0]:
                # print(insert_idx)
                first_lst[i:i] = tmp_lst
                break
            if i == len(first_lst)-1:
                first_lst.extend(tmp_lst)
        # print(first_lst)

    print('#{} {}'.format(test_case, ' '.join(map(str, first_lst[-1:-11:-1]))))